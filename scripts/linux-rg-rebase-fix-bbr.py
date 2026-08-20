#!/usr/bin/env python3
"""Finish leftover 7.1 BBRv3 tail hunks in net/ipv4/tcp_bbr.c."""
import sys
from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if new in text and old not in text:
        print(f"ok already: {label}")
        return text
    if old not in text:
        raise SystemExit(f"missing anchor: {label}")
    print(f"fixed: {label}")
    return text.replace(old, new, 1)


def main() -> None:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    path = root / "net/ipv4/tcp_bbr.c"
    text = path.read_text()

    text = replace_once(
        text,
        """__bpf_kfunc static void bbr_cwnd_event_tx_start(struct sock *sk)
{
	struct tcp_sock *tp = tcp_sk(sk);
	struct bbr *bbr = inet_csk_ca(sk);

	if (tp->app_limited) {
		bbr->idle_restart = 1;
		bbr->ack_epoch_mstamp = tp->tcp_mstamp;
		bbr->ack_epoch_acked = 0;
		/* Avoid pointless buffer overflows: pace at est. bw if we don't
		 * need more speed (we're restarting from idle and app-limited).
		 */
		if (bbr->mode == BBR_PROBE_BW)
			bbr_set_pacing_rate(sk, bbr_bw(sk), BBR_UNIT);
		else if (bbr->mode == BBR_PROBE_RTT)
			bbr_check_probe_rtt_done(sk);
	} else if ((event == CA_EVENT_ECN_IS_CE ||
		    event == CA_EVENT_ECN_NO_CE) &&
		   bbr_can_use_ecn(sk) &&
		   bbr_param(sk, precise_ece_ack)) {
		u32 state = bbr->ce_state;
		dctcp_ece_ack_update(sk, event, &bbr->prior_rcv_nxt, &state);
		bbr->ce_state = state;
	} else if (event == CA_EVENT_TLP_RECOVERY &&
		   bbr_param(sk, loss_probe_recovery)) {
		bbr_run_loss_probe_recovery(sk);
	}
}
""",
        """__bpf_kfunc static void bbr_cwnd_event_tx_start(struct sock *sk)
{
	struct tcp_sock *tp = tcp_sk(sk);
	struct bbr *bbr = inet_csk_ca(sk);

	if (!tp->app_limited)
		return;
	bbr->idle_restart = 1;
	bbr->ack_epoch_mstamp = tp->tcp_mstamp;
	bbr->ack_epoch_acked = 0;
	if (bbr->mode == BBR_PROBE_BW)
		bbr_set_pacing_rate(sk, bbr_bw(sk), BBR_UNIT);
	else if (bbr->mode == BBR_PROBE_RTT)
		bbr_check_probe_rtt_done(sk);
}

__bpf_kfunc static void bbr_cwnd_event(struct sock *sk, enum tcp_ca_event event)
{
	struct bbr *bbr = inet_csk_ca(sk);

	if ((event == CA_EVENT_ECN_IS_CE || event == CA_EVENT_ECN_NO_CE) &&
	    bbr_can_use_ecn(sk) && bbr_param(sk, precise_ece_ack)) {
		u32 state = bbr->ce_state;

		dctcp_ece_ack_update(sk, event, &bbr->prior_rcv_nxt, &state);
		bbr->ce_state = state;
	} else if (event == CA_EVENT_TLP_RECOVERY &&
		   bbr_param(sk, loss_probe_recovery)) {
		bbr_run_loss_probe_recovery(sk);
	}
}
""",
        "tcp_bbr.c cwnd_event split",
    )

    # drop leftover BBR1 tail that duplicates sndbuf and calls missing helpers
    text = replace_once(
        text,
        """__bpf_kfunc static u32 bbr_sndbuf_expand(struct sock *sk)
{
	/* Provision 3 * cwnd since BBR may slow-start even during recovery. */
	return 3;
}

/* In theory BBR does not need to undo the cwnd since it does not
 * always reduce cwnd on losses (see bbr_main()). Keep it for now.
 */
__bpf_kfunc static u32 bbr_undo_cwnd(struct sock *sk)
{
	struct bbr *bbr = inet_csk_ca(sk);

	bbr->full_bw = 0;   /* spurious slow-down; reset full pipe detection */
	bbr->full_bw_cnt = 0;
	bbr_reset_lt_bw_sampling(sk);
	return tcp_snd_cwnd(tcp_sk(sk));
}
""",
        """static void bbr_note_loss(struct sock *sk)
{
	struct tcp_sock *tp = tcp_sk(sk);
	struct bbr *bbr = inet_csk_ca(sk);

	if (!bbr->loss_in_round)
		bbr->loss_round_delivered = tp->delivered;
	bbr->loss_in_round = 1;
	bbr->loss_in_cycle = 1;
}

static void bbr_run_loss_probe_recovery(struct sock *sk)
{
	struct tcp_sock *tp = tcp_sk(sk);
	struct bbr *bbr = inet_csk_ca(sk);
	struct rate_sample rs = {0};

	bbr_note_loss(sk);
	if (!bbr->bw_probe_samples)
		return;
	rs.lost = 1;
	rs.tx_in_flight = bbr->inflight_latest + rs.lost;
	rs.is_app_limited = tp->tlp_orig_data_app_limited;
	if (bbr_is_inflight_too_high(sk, &rs))
		bbr_handle_inflight_too_high(sk, &rs);
}

__bpf_kfunc static u32 bbr_undo_cwnd(struct sock *sk)
{
	struct bbr *bbr = inet_csk_ca(sk);

	bbr_reset_full_bw(sk);
	bbr->loss_in_round = 0;
	bbr->bw_lo = max(bbr->bw_lo, bbr->undo_bw_lo);
	bbr->inflight_lo = max(bbr->inflight_lo, bbr->undo_inflight_lo);
	bbr->inflight_hi = max(bbr->inflight_hi, bbr->undo_inflight_hi);
	bbr->try_fast_path = 0;
	return bbr->prior_cwnd;
}
""",
        "tcp_bbr.c undo_cwnd",
    )

    text = replace_once(
        text,
        """__bpf_kfunc static void bbr_set_state(struct sock *sk, u8 new_state)
{
	struct bbr *bbr = inet_csk_ca(sk);

	if (new_state == TCP_CA_Loss) {
		struct rate_sample rs = { .losses = 1 };

		bbr->prev_ca_state = TCP_CA_Loss;
		bbr->full_bw = 0;
		bbr->round_start = 1;	/* treat RTO like end of a round */
		bbr_lt_bw_sampling(sk, &rs);
	}
}
""",
        """__bpf_kfunc static void bbr_set_state(struct sock *sk, u8 new_state)
{
	struct tcp_sock *tp = tcp_sk(sk);
	struct bbr *bbr = inet_csk_ca(sk);

	if (new_state == TCP_CA_Loss) {
		bbr->prev_ca_state = TCP_CA_Loss;
		tcp_plb_update_state_upon_rto(sk, &bbr->plb);
		bbr_reset_full_bw(sk);
		if (!bbr_is_probing_bandwidth(sk) && bbr->inflight_lo == ~0U)
			bbr->inflight_lo = max(tcp_snd_cwnd(tp), bbr->prior_cwnd);
	} else if (bbr->prev_ca_state == TCP_CA_Loss &&
		   new_state != TCP_CA_Loss) {
		bbr_exit_loss_recovery(sk);
	}
}
""",
        "tcp_bbr.c set_state",
    )

    text = replace_once(
        text,
        "	.cwnd_event_tx_start	= bbr_cwnd_event_tx_start,\n",
        "	.cwnd_event		= bbr_cwnd_event,\n"
        "	.cwnd_event_tx_start	= bbr_cwnd_event_tx_start,\n",
        "tcp_bbr.c cwnd_event op",
    )

    # drop the now-redundant forward declaration if the definition is above uses
    path.write_text(text)
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
