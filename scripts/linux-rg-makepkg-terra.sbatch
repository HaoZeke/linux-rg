#!/bin/bash
#SBATCH --job-name=linux-rg-pkg
#SBATCH --partition=cpu
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=12
#SBATCH --mem=20G
#SBATCH --time=06:00:00
#SBATCH --output=linux-rg-pkg-%j.out
#
# Arch linux-rg makepkg on rg.terra. One profile per invocation.
# Usage: LINUX_RG_PROFILE=rgx1gen11 sbatch scripts/linux-rg-makepkg-terra.sbatch
set -euo pipefail

profile=${LINUX_RG_PROFILE:-rgx1gen11}
case "$profile" in
  rgx1gen11|rgam5terra|rgSURFLat|rglat5340) ;;
  *) printf 'unsupported linux-rg profile: %s\n' "$profile" >&2; exit 2 ;;
esac

root=${LINUX_RG_ROOT:-$HOME/tmp/linux-rg-718}
repo=${LINUX_RG_REPO:-$root/src}
srcdest=${LINUX_RG_SRCDEST:-$root/srcdest}
builddir=${LINUX_RG_BUILDDIR:-$root/build-$profile}
pkgdest=${LINUX_RG_PKGDEST:-$root/pkgdest}
logdir=${LINUX_RG_LOGDIR:-$root}
jobs=${SLURM_CPUS_PER_TASK:-${LINUX_RG_JOBS:-12}}
toolchain=${LINUX_RG_RUST_TOOLCHAIN:-1.97.1}

mkdir -p "$srcdest" "$builddir" "$pkgdest" "$logdir" "$logdir/tmp-$profile"

if [[ ! -f $repo/PKGBUILD ]]; then
  printf 'missing PKGBUILD in %s\n' "$repo" >&2
  exit 2
fi

export PATH="$HOME/.cargo/bin:/usr/bin:$PATH"
export RUSTUP_TOOLCHAIN="$toolchain"
if command -v rustup >/dev/null 2>&1; then
  rustup component add rust-src --toolchain "$toolchain"
fi

echo "host=$(hostname) job=${SLURM_JOB_ID:-none} profile=$profile rustc=$(rustc --version)"
echo "repo=$repo builddir=$builddir pkgdest=$pkgdest jobs=$jobs"
date -Is
free -h
df -h "$builddir" "$pkgdest"

cd "$repo"
env \
  LINUX_RG_PROFILE="$profile" \
  MAKEFLAGS="-j${jobs}" \
  SRCDEST="$srcdest" \
  BUILDDIR="$builddir" \
  PKGDEST="$pkgdest" \
  TMPDIR="$logdir/tmp-$profile" \
  PACKAGER="linux-rg remote <rgoswami@ieee.org>" \
  makepkg --nodeps --skippgpcheck --cleanbuild --log \
    --config /etc/makepkg.conf

date -Is
echo "packages:"
ls -lh "$pkgdest"/linux-rg-*.pkg.tar.*
python3 - "$pkgdest" "$profile" <<'PY'
import glob, os, sys, tarfile
pkgdest, profile = sys.argv[1], sys.argv[2]
pkgs = sorted(glob.glob(os.path.join(pkgdest, "linux-rg-7.1.8.arch1-4-x86_64.pkg.tar.*")))
if not pkgs:
    raise SystemExit("missing linux-rg package")
pkg = pkgs[-1]
want = "usr/lib/modules/"
found = False
with tarfile.open(pkg) as tf:
    for name in tf.getnames():
        if name.endswith("nft_socket.ko.zst") or name.endswith("nft_socket.ko"):
            print("packed", name)
            found = True
            break
if not found:
    raise SystemExit(f"{pkg} has no nft_socket module")
print("nft_socket present in", os.path.basename(pkg), "profile", profile)
PY
