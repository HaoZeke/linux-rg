# linux-rg

`linux-rg` is an Arch Linux kernel package with support for multiple machine
profiles. It follows Arch's `linux` PKGBUILD layout and produces `linux-rg` plus
`linux-rg-headers`.

The package starts from the upstream Arch source and `config.x86_64`, then
applies a small machine-specific overlay (e.g. `rgx1gen11.config`). Shared patch
series live at the repo root; each profile contributes its own config overlay
and hardware-specific validation.

## Machine profiles

| Slug       | Form factor | CPU / GPU                  | Status     | Key files                  |
|------------|-------------|----------------------------|------------|----------------------------|
| rgx1gen11  | Laptop      | Intel i7-1365U / Iris Xe   | Active     | rgx1gen11.config + docs    |
| rgam5terra | Desktop     | Ryzen 9 9950X / ASUS RTX 5070 Dual / B650I Terra | Researching | MC receipts in targets.org |

- Shared research evidence and candidate evaluation: `docs/literature-review.org`, `docs/candidates.org`
- Per-profile hardware targets, drivers, boot contracts, and patch applicability notes live in the profile-specific docs.
- The patch stack (0001-*.patch) is evaluated for one or more profiles; applicability is tracked in candidates.org and per-profile targets.

Current focus: rgx1gen11 (daily driver). rgam5terra (AM5/RTX) profile docs and
vissues feed both the Archiso selector and NixOS provisioning evaluation.

## Selected Changes (current carry set)

The changes below are the currently carried set. Most were motivated by the
rgx1gen11 profile; applicability to other profiles (e.g. rgam5terra) is tracked
in =docs/candidates.org= and the per-profile kernel/targets docs.

- BORE from the CachyOS patch set, adapted for Arch 7.0 fair scheduler layout.
- BBRv3 from the CachyOS patch set, adapted for the Arch 7.0 TCP layout.
- v4l2loopback from pf-kernel, built in-tree as `CONFIG_V4L2_LOOPBACK=m`.
- DDCCI and DDCCI backlight support from `ddcci-driver-linux`, built in-tree.
- CachyOS block-layer contention patch for BFQ and mq-deadline.
- Scheduler weld for hybrid i7-1365U (rgx1gen11): hot-path inlines (0010),
  detach_tasks fix (0011), sched_ext SMT idle (0012), migration_cost sysctl (0013).
- Cache-aware fair-class placement experiment (0020), enabled as
  `CONFIG_SCHED_CACHE=y` for LLC locality testing on the hybrid CPU (rgx1gen11).
- Liquorix zen cherry-picks (no PDS): kswapd_waiters MM fix (0014), schedutil
  DL limits_changed (0015). iwlwifi/i915 zen hunks skipped -- already in Arch 7.0.12.
- ADIOS block scheduler module (non-default) and ASA sched_ext router prototype
  (arXiv:2511.11628) with `asa-router` userspace helper.
- PSI, memcg, DAMON, MGLRU, KSM, zswap, zram, BFQ, sched_ext, and
  platform support pinned in per-profile config overlays (rgx1gen11 example:
  ThinkPad/Intel laptop paths).
- Compression policy support: zswap defaults to zstd, zram writeback/tracking is
  available, and the installed kernel keeps zstd modules available for compressed
  memory, initramfs, module, and btrfs policy work.
- Pstore crash evidence support: EFI pstore is compiled in but disabled by
  default, pstore compression is enabled, and ramoops/pstore-blk remain modular
  for tested crash-log escalation.
- CachyOS working-set protection ratio extract (0018): `vm.anon_min_ratio`,
  `vm.clean_low_ratio`, `vm.clean_min_ratio`, and `vm.workingset_protection`
  wired into classic reclaim and MGLRU without carrying `CONFIG_CACHY`.
- MGLRU dev-tree vmscan weld (0019): writeback handling helper, evictable-size
  scan budgeting, and batch eviction flow adapted to keep the 0018 ratio gates.
- MM bulk-free hot paths (0021): `free_contig_range()` and `vfree()` batched
  page freeing carried for memory-pressure benchmarking.
- Intel AX211 Wi-Fi/BT: `IWLMLD`, `bt_coex_active` modprobe drop-in; `linux-firmware`
  in package depends; `rgx1gen11-ax211-check` validates the config, module tree,
  modprobe policy, and firmware inventory.
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

For `rgx1gen11`, the build recipe applies `rgx1gen11.lsmod` through
`localmodconfig` before the profile overlay. The overlay then re-pins the boot,
input, GPU, Wi-Fi, Bluetooth, audio, camera, DDC/CI, pstore, and sched-ext
contracts. `LINUX_RG_MODULE_BUDGET` defaults to `1500` for this profile so a
broad Arch-style module build fails during `prepare()` instead of during final
module linking.

## Hardware Checks

Validate the AX211 policy from the repo config:

```sh
./rgx1gen11-ax211-check
```

Validate a prepared build tree before packaging:

```sh
./rgx1gen11-ax211-check \
  --config /path/to/linux-7.0.12/.config
```

Validate an installed linux-rg boot:

```sh
rgx1gen11-ax211-check --live
```

Validate the PSI/MGLRU/DAMON/zram memory-pressure contract:

```sh
./rgx1gen11-memory-check
rgx1gen11-memory-check --live --require-oomd
```

The same checker asserts the pstore crash-log config contract. Active pstore
backend selection is tracked separately so EFI-variable writes are not enabled
blindly.

Inspect pstore post-boot evidence and `systemd-pstore` state:

```sh
rgx1gen11-pstore-check
```

Validate the cpuidle/intel_idle/TEO contract:

```sh
./rgx1gen11-idle-check
rgx1gen11-idle-check --live
```

Validate the Iris Xe i915/xe boot-driver contract:

```sh
./rgx1gen11-gpu-check
rgx1gen11-gpu-check --live --require-boot-log
```

Validate the SOF + HDA audio contract:

```sh
./rgx1gen11-sof-check
rgx1gen11-sof-check --live --require-boot-log
```

Validate the KIOXIA XG8 NVMe/APST contract:

```sh
./rgx1gen11-nvme-check
rgx1gen11-nvme-check --live
```

Validate the encrypted btrfs hibernate path and image-size cap:

```sh
./rgx1gen11-hibernate-check --live
rgx1gen11-hibernate-image-size status
```

Validate S2idle/S0ix diagnostic prerequisites before running Intel's root-only
S0ixSelftestTool:

```sh
rgx1gen11-s0ix-tool-sync
rgx1gen11-s0ix-preflight
```

The sync helper clones or updates Intel's S0ixSelftestTool under
`${XDG_CACHE_HOME:-$HOME/.cache}/rg-kernel/S0ixSelftestTool` and prints the
root commands for suspend and runtime PC10 checks. If the user cache is not
writable, it falls back to `/tmp/rg-kernel/S0ixSelftestTool`; set
`S0IX_TOOL_FALLBACK_ROOT=/path` to choose another writable root. The preflight
also accepts `S0IX_TOOL=/path/to/s0ix-selftest-tool.sh` for an existing
checkout. Non-root preflight treats root-only PMC debugfs access as an
actionable root-required state; use `RGX1GEN11_STRICT_PMC=1` when a caller
needs unreadable PMC counters to fail.

## Install for rEFInd

After a successful build, install the generated packages, create the linux-rg
mkinitcpio preset, and add a non-default rEFInd stanza:

```sh
scripts/rgx1gen11-install-refind-root --dry-run
sudo bash scripts/rgx1gen11-install-refind-root
```

By default the installer discovers the newest `linux-rg` and
`linux-rg-headers` packages under
`~/.local/share/rg-kernel/artifacts/linux-rg`. Under `sudo`, it resolves that
path from `SUDO_USER` rather than root's home directory. Override with
`LINUX_RG_ARTIFACT_DIR`, `LINUX_RG_KERNEL_PKG`, or `LINUX_RG_HEADERS_PKG` when
testing a different build output.

The script keeps the stock Arch entry intact and inserts `Arch Linux linux-rg`
after it. It copies `/usr/lib/modules/*-rg/vmlinuz` to `/boot/vmlinuz-linux-rg`
and writes `/boot/initramfs-linux-rg.img` from a separate mkinitcpio config with
`MODULES=(nvme i915)`.

The dry-run is a hardware probe. It refuses to proceed unless the live machine
matches the rgx1gen11 boot contract: encrypted btrfs root on `/dev/mapper/luks`,
the stock rEFInd command line carries `cryptdevice=`, `rootflags=subvol=@`,
`resume=`, `resume_offset=`, standalone `i915`, and `pcie_aspm.policy=powersave`,
the linux-rg initramfs keeps early `nvme i915`, and `/etc/vconsole.conf` uses
`KEYMAP=colemak` so the LUKS prompt remains typeable.

The installer also enables `rgx1gen11-hibernate-image-size.service`, which sets
`/sys/power/image_size` to 8 GiB at boot. This keeps the hibernate image below
the btrfs swapfile capacity and reduces suspend-to-disk write volume for laptop
workflows.

Validate the installer dry-run and package discovery path without root:

```sh
bash scripts/rgx1gen11-install-refind-root-selftest
scripts/rgx1gen11-install-refind-root --dry-run
```

After selecting `Arch Linux linux-rg` in rEFInd:

```sh
rgx1gen11-live-check --with-userspace
```

If the package is already built and the installed tree needs to be repaired
without rebuilding, run the reinstall verifier from the checkout:

```sh
scripts/rgx1gen11-reinstall-check-root --dry-run
sudo bash scripts/rgx1gen11-reinstall-check-root
```

The script validates the package payload, trashes only known rEFInd screenshots
and `FSCK*.REC` files from `/boot`, reinstalls `linux-rg` and
`linux-rg-headers`, rebuilds the linux-rg initramfs, runs
`rgx1gen11-boot-check --installed`, and checks pacman file ownership.

## DKMS Overlays

The package ships compatibility overlays for out-of-tree modules that lag the
Linux 7.0 kernel API:

- `ddcci/0.4.5`
- `rtl88xxau/r1298.b44d288`
- `evdi/1.14.7`

After installing `linux-rg` and `linux-rg-headers`, apply the overlays and
rebuild the modules for the installed kernel:

```sh
sudo RG_DKMS_JOBS=9 rgx1gen11-dkms-overlay-apply 7.0.12-arch1-1-rg
```

The helper backs up the DKMS sources under
`/tmp/rg-linux-rg-dkms-overlay-backups`, patches both `/usr/src` and active
`/var/lib/dkms/*/build` trees idempotently, then runs `dkms build`, `dkms
install`, and `depmod` for the target kernel.

## Notes

### Profile docs

- `docs/profiles.org` -- index of machine profiles, hardware summaries, and applicability map
- `docs/rgx1gen11-kernel.org` -- rgx1gen11 profile + carried patches rationale
- `docs/rgx1gen11-targets.org` -- verified hardware inventory, workload profiles, targets
- `docs/rgx1gen11-drivers.org` -- driver map for the profile
- `docs/rgx1gen11-boot-safety.org` -- rollback and mkinitcpio contract (read first for the profile)

Shared evidence (applies across profiles unless noted):

- `docs/literature-review.org` -- research sources, evidence grades, venue map
- `docs/candidates.org` -- patch and policy candidates with per-profile applicability notes

### Issue tracking (vissues)

```sh
vissue ready --root ~/Git/Gitlab/obsidian-notes --project linux-rg
vissue tree --root ~/Git/Gitlab/obsidian-notes linux-rg-ln3w
```

Vault file: `~/Git/Gitlab/obsidian-notes/Software/linux-rg/issues.org`

### Patch and policy rules

Patch carry decisions are intentionally narrow: selected patches must apply
reproducibly, compile against the Arch kernel base, and have documented
applicability to one or more active profiles (see candidates.org and the
profile targets docs).

rgam5terra profile docs include a CachyOS/sirlucjan downstream patch survey.
=0022-amd-znver5-rdseed.patch= is profile-gated for the Zen 5 build. Archiso
profile-selector behavior is tracked in =linux-rg-1xe1=, and NixOS provisioning
evaluation is tracked in =linux-rg-gdg7=.
