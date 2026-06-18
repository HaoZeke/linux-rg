# linux-rg

`linux-rg` is an Arch Linux kernel package for a ThinkPad X1 Carbon Gen 11,
model `21HM002GUS`, with an Intel Core i7-1365U, Intel Iris Xe graphics, Intel
CNVi Wi-Fi, Thunderbolt 4, and KIOXIA XG8 NVMe storage.

The package follows Arch's `linux` PKGBUILD layout and produces `linux-rg` plus
`linux-rg-headers`. It keeps the upstream Arch source and config as the base,
then applies a small machine overlay in `rgx1gen11.config`.

## Selected Changes

- BORE from the CachyOS patch set, adapted for Arch 7.0 fair scheduler layout.
- BBRv3 from the CachyOS patch set, adapted for the Arch 7.0 TCP layout.
- v4l2loopback from pf-kernel, built in-tree as `CONFIG_V4L2_LOOPBACK=m`.
- DDCCI and DDCCI backlight support from `ddcci-driver-linux`, built in-tree.
- CachyOS block-layer contention patch for BFQ and mq-deadline.
- Scheduler weld for hybrid i7-1365U: hot-path inlines (0010), detach_tasks fix
  (0011), sched_ext SMT idle (0012), migration_cost sysctl (0013).
- Liquorix zen cherry-picks (no PDS): kswapd_waiters MM fix (0014), schedutil
  DL limits_changed (0015). iwlwifi/i915 zen hunks skipped -- already in Arch 7.0.12.
- ADIOS block scheduler module (non-default) and ASA sched_ext router prototype
  (arXiv:2511.11628) with `asa-router` userspace helper.
- PSI, memcg, DAMON, MGLRU, KSM, zswap, zram, BFQ, sched_ext, and
  ThinkPad/Intel laptop support pinned in the machine config overlay.
- Intel AX211 Wi-Fi/BT: `IWLMLD`, `bt_coex_active` modprobe drop-in; `linux-firmware`
  in package depends.
- BBR and fq selected as the default TCP congestion control and qdisc.

## Build

Use home-backed build and compiler temporary directories; `/tmp` is too small for a full kernel build
on this machine.

```sh
cd ~/Git/Github/Tools/linux-rg
env GNUPGHOME=${GNUPGHOME:-/home/rgoswami/.local/share/chezmoi/.kernel-build/gnupg} \
  MAKEFLAGS=-j9 \
  TMPDIR=/home/rgoswami/.local/share/chezmoi/.kernel-build/tmp \
  BUILDDIR=/home/rgoswami/.local/share/chezmoi/.kernel-build/linux-rg-build \
  PKGDEST=/home/rgoswami/.local/share/chezmoi/.kernel-build/pkgdest \
  makepkg --nodeps --cleanbuild --clean --log
```

`-j9` keeps the local build under the configured 80% CPU cap for this 12-thread
machine.

## Notes

Design, hardware targets, and patch rationale:

- `docs/rgx1gen11-boot-safety.org` -- **read before first boot** (rollback, mkinitcpio)
- `docs/rgx1gen11-drivers.org` -- Wi-Fi/BT/GPU/audio/NVMe/TB4 driver map
- `docs/rgx1gen11-targets.org` -- verified hardware inventory, workload profiles,
  measurable targets, vissue map
- `docs/rgx1gen11-kernel.org` -- machine profile and carried patches
- `docs/literature-review.org` -- research bibliography and evidence grades
- `docs/candidates.org` -- ADIOS, re-swappiness, cpuidle TEO, detach_tasks, and
  other candidate notes

Issue tracking (vissues):

```sh
vissue ready --root ~/Git/Gitlab/obsidian-notes --project linux-rg
vissue tree --root ~/Git/Gitlab/obsidian-notes linux-rg-ln3w
```

Vault file: `~/Git/Gitlab/obsidian-notes/Software/linux-rg/issues.org`

Patch carry decisions are intentionally narrow: selected patches must apply
reproducibly, compile against the Arch kernel base, and match this laptop's use
cases.
