let meta = #{
    name: "linux-rg-net-dead-vote",
    description: "Five-node raft vote on why linux-rg boot had dead ping and APIs",
    when_to_use: "After linux-rg-b2qh is filed; vote the cause among child ids",
    phases: [
        #{ title: "Vote", detail: "five independent cause votes" },
    ],
};

let vote_schema = #{
    "type": "object",
    "required": ["cause_id", "accept_leading", "evidence", "gaps"],
    "properties": #{
        "cause_id": #{ "type": "string" },
        "accept_leading": #{ "type": "boolean" },
        "evidence": #{ "type": "string" },
        "gaps": #{ "type": "string" },
    },
};

let root = ".";
let scope = "";
if args != () {
    if args.root != () { root = args.root; }
    if args.scope != () { scope = args.scope; }
}
if root == "." { pause("verification", "Pass args.root — linux-rg checkout."); }
if scope == "" { pause("verification", "Pass args.scope — parent ticket id."); }

phase("Vote");
let jobs = [];
let n = 1;
while n <= 5 {
    let p = "";
    p += "You are Raft diagnosis voter " + n.to_string() + " of 5.\n";
    p += "Read-only. Checkout " + root + "\n";
    p += "Parent ticket: " + scope + "\n";
    p += "Open the project issue tracker for " + scope + " and its children. Use the local tracker CLI if present.\n";
    p += "Allowed cause_id values (pick exactly one):\n";
    p += "linux-rg-0jwr Houston fail-closed dests after rg-us-egress-up assert EINVAL\n";
    p += "linux-rg-frcl localmodconfig pruned IP_ROUTE_CLASSID and nft extras\n";
    p += "linux-rg-fj1n DNS rewrite not rolled back when Houston up fails\n";
    p += "linux-rg-pxky iwlwifi firmware or AX211 driver failed\n";
    p += "linux-rg-cyuh BBRv3 default congestion control broke reachability\n";
    p += "Use grep and read_file on the checkout. Confirm journal facts from the parent body against scripts/rgx1gen11-network-policy-check, rgx1gen11.config, and docs/rgx1gen11-kernel.org.\n";
    p += "cause_id must be one of the five ids above. accept_leading=true only if your cause_id is linux-rg-0jwr.\n";
    p += "evidence must cite file:line or a journal timestamp already in the parent body. Comments are not evidence.\n";
    p += "Do not cargo build. Do not invent new ticket ids in cause_id. gaps is empty string if none.\n";
    p += "If two causes compose, pick the one that explains ping timeout AND dead APIs on that boot. Secondary causes go in gaps as already-filed ids only.\n";
    jobs.push(#{
        prompt: p,
        label: "vote-" + n.to_string(),
        capability_mode: "read-only",
        output_schema: vote_schema,
    });
    n += 1;
}
let votes = parallel(jobs);
let tallies = #{};
let seen = 0;
let yes_leading = 0;
let gaps = "";
for v in votes {
    if v != () && v.success && v.output.cause_id != () {
        seen += 1;
        let cid = v.output.cause_id;
        if tallies[cid] == () { tallies[cid] = 0; }
        tallies[cid] = tallies[cid] + 1;
        if v.output.accept_leading == true { yes_leading += 1; }
        if v.output.gaps != () && v.output.gaps != "" {
            gaps += v.output.gaps;
            gaps += "\n";
        }
        if v.output.evidence != () {
            gaps += "evidence: ";
            gaps += v.output.evidence;
            gaps += "\n";
        }
    }
}
let winner = "";
let win_n = 0;
for cid in ["linux-rg-0jwr", "linux-rg-frcl", "linux-rg-fj1n", "linux-rg-pxky", "linux-rg-cyuh"] {
    if tallies[cid] != () && tallies[cid] > win_n {
        win_n = tallies[cid];
        winner = cid;
    }
}
let committed = seen >= 5 && win_n >= 3;
let rpt = "# linux-rg-net-dead-vote\n\n";
rpt += "scope=" + scope + "\n";
rpt += "committed=" + committed.to_string() + " seen=" + seen.to_string() + "\n";
rpt += "winner=" + winner + " votes=" + win_n.to_string() + "\n";
rpt += "yes_leading=" + yes_leading.to_string() + "\n";
rpt += gaps;
let pth = write_scratch_file("net-dead-vote.md", rpt);
complete(#{ path: pth, ok: committed, winner: winner, win_n: win_n, seen: seen, scope: scope });
