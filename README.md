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
- PSI, memcg, MGLRU, KSM, zswap, zram, BFQ, sched_ext, and ThinkPad/Intel
  laptop support pinned in the machine config overlay.
- BBR and fq selected as the default TCP congestion control and qdisc.

## Build

Use a home-backed build directory; `/tmp` is too small for a full kernel build
on this machine.

```sh
env GNUPGHOME=/tmp/linux-rg/.gnupg \
  MAKEFLAGS=-j9 \
  BUILDDIR=/home/rgoswami/.local/share/chezmoi/.kernel-build/linux-rg-build \
  PKGDEST=/home/rgoswami/.local/share/chezmoi/.kernel-build/pkgdest \
  makepkg --nodeps --cleanbuild --clean --log
```

`-j9` keeps the local build under the configured 80% CPU cap for this 12-thread
machine.

## Notes

The design rationale is in `docs/rgx1gen11-kernel.org`. Patch carry decisions
are intentionally narrow: selected patches must apply reproducibly, compile
against the Arch kernel base, and match this laptop's use cases.
