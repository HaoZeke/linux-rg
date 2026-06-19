# Maintainer: Jan Alexander Steffens (heftig) <heftig@archlinux.org>

pkgbase=linux-rg
pkgver=7.0.12.arch1
pkgrel=1
pkgdesc='Linux kernel for rgx1gen11 ThinkPad X1 Carbon Gen 11'
url='https://github.com/archlinux/linux'
arch=(
  x86_64
)
license=(GPL-2.0-only)
makedepends=(
  bc
  binutils
  cpio
  gettext
  glibc
  libelf
  libgcc
  openssl
  pahole
  perl
  python
  rust
  rust-bindgen
  rust-src
  tar
  xxhash
  xz
  zlib
  zstd

)
options=(
  !debug
  !strip
)
_srcname=linux-${pkgver%.*}
_srctag=v${pkgver%.*}-${pkgver##*.}
source=(
  https://cdn.kernel.org/pub/linux/kernel/v${pkgver%%.*}.x/${_srcname}.tar.{xz,sign}
  $url/releases/download/$_srctag/linux-$_srctag.patch.zst{,.sig}
  0001-bore-cachy.patch
  0002-bore-fair-arch-adapt.patch
  0003-bbr3-cachy.patch
  0004-bbr3-arch7-adapt.patch
  0005-v4l2loopback-pf.patch
  0006-ddcci-driver.patch
  0007-block-cachy.patch
  0008-adios-cachy.patch
  0009-asa-sched-router.patch
  0010-cachy-hotpath-inline.patch
  0011-detach-tasks-fix.patch
  0012-sched-ext-smt-idle.patch
  0013-sched-migration-cost.patch
  0014-zen-kswapd-waiters.patch
  0015-zen-schedutil-limits.patch
  0016-cpuidle-teo-default.patch
  0017-bbr3-tcp-prototype.patch
  0018-cachy-mm-ratios.patch
  0019-mglru-devtree-adapt.patch
  0020-cache-aware-sched.patch
  0021-mm-bulk-free-hotpaths.patch
  rgx1gen11.config
  asa-router
  rgx1gen11-ax211-check
  rgx1gen11-memory-check
  rgx1gen11-pstore-check
  rgx1gen11-idle-check
  rgx1gen11-gpu-check
  rgx1gen11-sof-check
  rgx1gen11-nvme-check
  rgx1gen11-hibernate-check
  rgx1gen11-hibernate-image-size
  rgx1gen11-hibernate-image-size.service
  rgx1gen11-s0ix-preflight
  rgx1gen11-s0ix-tool-sync
  rgx1gen11-boot-check
  rgx1gen11-iwlwifi.conf
  rgx1gen11-btusb.conf
)
source_x86_64=(config.x86_64)
validpgpkeys=(
  ABAF11C65A2970B130ABE3C479BE3E4300411886  # Linus Torvalds
  647F28654894E3BD457199BE38DBBDC86092693E  # Greg Kroah-Hartman
  83BC8889351B5DEBBB68416EB8AC08600F108CDF  # Jan Alexander Steffens (heftig)
)
sha256sums=('57edc9a41efc1ca6b797afa8f4a587a30da2af6bca7356eb56e1e1a4ada265da'
            'SKIP'
            'ce38af1268931b099993cf01c537d6c3b21007e08cad84d2f1e71f95cc5cb75b'
            'SKIP'
            'f594e3a0cf55649377e09bc22e6dd5152ecafe6a96460a68036a35bba5ba932e'
            '12e8cf31882138d0c90a59d8e2ad863ce87099fa300dded743a32887ccc2ad90'
            '8ea77c5038568d79d54319c7277363686c1ae44f927d3bf2f0d65c4ec2bad91f'
            '14ec55043d8247468aa5ccac6fde85096ff89b0182598d9d896d498acef784bd'
            '4552ccbf50e5a7c45c7f70ca8db55a444584c99c53f61ec42c74ced68ffd4658'
            'd8ae5e09265e87370655a672156bf95b9cdc3b85acc19d9b82fbf4e895efedd0'
            '1c9c4cfda09760a06927574e74e4094193d081dfb9b81e3a958379c60c17272b'
            '0fb154e8401fa57055e184b6fe922a6a81c3d5ae41e19d31548e548339839327'
            '5a99717aa7708a3b8715ec87065c7974fdbd55908a5e18c09861b972dc48bd08'
            '882c1b29e935d2bee1873c0ce135ea4ce1d91343a49f41d902ecaf8d9be8f9f8'
            '92c8bfd96f91ff0da27d7714360188da4e442aff1722830b1803770b9cd21a0d'
            '509246930ad9065f9d4c3a98ac267ad164f3233aa8769cdfe0d4c54ee602cad8'
            'be700356b32a79561e4e45c12b16cc7724bebdf82b1af4e8c9a7348351e8cc9c'
            '3102018370fd41d6beee22b579349bc9420495dac7eac89175b29a2d25fb7a54'
            'f936b1e3264284b87ffe25ddbde24e1f2cbd17337576767c4d630d7271fab0b0'
            '70f173e5682f791e2c2c7974fe46cb36c3247e770de664b238a6786c20c22c9c'
            '61de8fb699c581eeb81b24c6f21445035a8660155ca7ddcf7ced11c7d6a10cc3'
            'f7afb212766a7563f45cf0703f3c3b8cdded875f9624a972832d05ba87bde377'
            '168a5264f9be2654889554a561a746c37df3e9c021e5bea7ff638d36f5341c8b'
            'e9f56c6b5022ecab01b8ae7fa619c5d0f36b8254db5dfcb757b60b2868a3d567'
            'c6deacb47a8ca1185d379a164e9579413a843285090e5778fe54395b76efbe71'
            'e366456854183ab5c0389715f7c34e502c40b2d0b63a29b42b7bcde5b51fb874'
            'fa9059e8274b60d3caf1d5e78a1fe21b92d937fe21562df5920b9c66d0013923'
            'ae73ca4affd8a3dd9a46d710774268e085f6bbba8462bb1a65963301f36f0579'
            '7b499919d2f72a5d077d142562b5d89917953c3045821d50a2d736e4d8a02a51'
            '81f35cfa14c9883a13e75afa531f667edd27fdba0ad4925aabc57c886fee79e1'
            '7be77c35c385f81cf9d095f63e1a6c7f27af7470f8a4f0f4920ea3311833f1fa'
            'b844e14b2d67ae54959ed319ea02f8be260d11825474f233437f4309a213a907'
            '9729ea6489e47a4a585defd64e01beddc9133b9540214217875c1b2afaac26a9'
            '76c1b5054809401cf1eeb1cec9cc41aeb869aaf9e45a7857aacdd7cdbff7168c'
            'a004b98e2f4cd1b4eec8b01ebb3f43c51c4b763fa2634cc73c9a7ba41063102c'
            'ea33da5db83296ee3313a060b746e11c184fbb3b60cfe5f5d52fe6d87523ae75'
            '99737bbda3820841aa904a95599cd126a974de262e340dca231b9b8cf8a4758c'
            '4fc1a92f7340561c70240ccf504950d7b389a59b9a4f888b0b91104417cd55d4'
            'd1b63c17576b26243c9c0cd9350679c22dbd2175e5af3612de977c3cf60ee286'
            '619d43e497595f4d30007082c24ba708d5a2828c277d4fdbb66de830b80e506a'
            '134551c9ab2a33011cd2cdf366e66da4cc9297011146a8abe8840f5b7a3f7408'
            '3ef3c4a79ef713154998cfecf47f66244ed81dd8d181b970f768e0a873e65e74')
sha256sums_x86_64=('0ed8c43b4ad6c3c3f3affe1317581992ba0eac6697d421a5c6d8210bf1e29ad7')
b2sums=('2c53f205a940b0f9f68653b92ef46d49f828cbef3cfa8cf94d050c8e6df05c4fcaa4f9b9681b9130b14e3c790d31208eb244d123249a93e35e8e6165f3d858c9'
        'SKIP'
        '26230d1a111b24fe9239273acdfacda37c5bf009f861c448ad25392dcca433514246d629a077ce5c66478c7e0f4e5477ce5f95c91d08b3a02cc87bb35b849bcf'
        'SKIP'
        '9dc1a5a46d8ecf606323926f22b4ce0aaf910dc47fd9ab9b8d08d1600e0bb45109babf7098f390562d8d8456239bb44b7db13b175fe2f529b9784a603dc11fbe'
        '82d0b6b7cbaf4cf6df3e9e57d618082743853eef62292e05f7b04f2aeace9d1e9861b8aa4f42ab16d9e19d0b21238d0431d4c735d557aef3153ec2f7e0c4b980'
        '582d2cc4c417ea20b5d361c469c0c1f70a1733dcdedb1e3f80b7339f19dc3229bd3ebe605c30955fce21973e51fff1de89bcd2d153eba43cc5b987b98397ccb8'
        'f80d355bd4f2875e55e3817d2853af4e5e9ee64703ec294a6d2a8244fbafce2fc152e1eee6539b1d6a2710f1148a7afe813b1aeb69a6b04f68821fa723cf1eab'
        'b4f108a878bfcebf5d765c7ef37a96ef4e76894c4453595aaca7a200dd65234572bf95b7bec8640af2c2f97534230e12c06a6330e853134932e22625308b3124'
        'b13e277497e8d688beb8e69bf8eac9e4b0f760d927a4c02b4b0fe80c8be43022dc3e8e5b68377827aca40fd03eefd648dc638e51024b837a9dd438448cbfa0a1'
        '1e03198bd2c832238c5d4dfc0fa742ea32db994f4a19bfde84745d40d77c85476aee1832b45d153d071fb124e967423fac112c1f8b4da38ac90458fd3e023493'
        'de2717075b6af543f888d2a6604180f0d256fa3abe0109efeaf876939ad186195d57b667dc5a757d97c4fdc77a1fca4f4499c144a82793d9cb7bc00db0ef5412'
        'c5586d7c26a3685822c745198635637573bf146180834b4435f1d0f059dbc5682e30d243f4496efb53b23629f1859abadf04a291feb502f52880af3458d5db42'
        'b2260db749e3632a80b6d45d8d0777e0cff8d481798c3b079364dfa327c14f7534960f082e3b37486413e6f89812e9e6ded4a9d17b8997d94da2522c5c69c18f'
        'c9ff8674f26e0bd49a1cbecbd7ef4ab76507ecca4d5d3e085fdbadf6c809fb652fa209395684e5042b28532cc723ac11083d48414aa7805536c199abfef33797'
        '3eff3a53ffc70df96b1a620883acd6fff4e0f875edf9191598957e40e028fca2f614d505faad410ac9d4fd1c0ebd0c048fa1c04383d069e1a1e4abc5ed2c9110'
        '43092dc75bf584705b4075be1a53a85833420c7e3a7ea55b02e9add1a33160f06bf497792a4f5dcd11be2e99eb5fa3a91f13ea79bb1873434350ac975dec2b72'
        '08e550a84c84df1059225a0096e5d829a223c695511464b753614c0102b60ba59f7960a35535459822a56ef434c89ee54601e813c0cf3d4985ea05f1e31e4561'
        '8ca24572f81b16fbb1138b7b4681e34c107b9e77bf031e69884a4abb0216aa666cf24215e5235276b15e335e397a3a42645103c1cb515f84f69172a145dddc85'
        'd15aab2d06223b62ba4a675f626539e6b75632cb5ba6820ba71fd2298dd9859eb4d83d614e44504e75f1aae4f6a78f1d8ef9f4f1eb135f79a5cd688fc4ce1253'
        'ad5190157b175dd7222aa739ce94b4f66b6319bad983c133381e4397c51ecea36d995623cd3f005b84a4998e9161089f66d45007187fc4a9ab1d7850b74ee1c1'
        'd8387b6a41444f849a99696b6980662607618afcd1a0feeeb31723c84cd25b04bef5c95d168b352f5d6f07911bf1b2e3a71a40ed7a63268e34045a7d57b7554f'
        'a816bd03d460ca3910fa4790ea7d945df0a3fa5adef85f681057e82a549aba959f0c3296853285a4d370faa222841ef8c1efe40bb41f0134e7806106d8723481'
        '5b9c44d3e1b13bcd7599ecc0b07d0af822bb83672876138f981374aba20b0f7f1475dadd06127e2c29596550f3ad8232a9f534f29810192d95ed6bd7ed279a73'
        'b8ff5dee5b81818ef02107990b5711a7a4d060a943a6663334e0ffa828dd52696bef62b79f2a9ceb369221db0e468d238c6d61ef7127a7b318dacf350f3bbfa6'
        '21921700ec720827040a878a9df667ea7640e590f0b7274b3f4d153cf6f62fc11be106223bccd199d8c8ccb45ca8ad837d9afffebcdd640196a5d3d76b080d9c'
        '4f290c4b5aeed7d8a2e048410f304c891955129c1641b5a1145302e61f1e9f76593448d9c765fc13e1717159245c9d304948087f79e04d69e53fdfea4a5e5f13'
        '9025bb521840b05518bb39fff120cc6ba8ee90b09886631cf9868a5731151b064fb2c8ac22ad910eeb1e32437785df97a3e2a3bd43581c314a6ff34bebca85e6'
        'd849a1125b3e5ebb4f43918da5f3cd67d2d1c704adb9b8642666e388bc6e763502784f82cf5e3e2b62888099e5d89573bc73ebb0f3a6f2d7475f03b72612dc1c'
        'c0efa28a08c225f90e40858319760ee1b6ebcfcaa8241ba996b5df61cd2e457e4dabe35dd4a9b49ed0243c1789902de8d82e4e73e4a02efbd89efcde8d3916d3'
        '1ccf13729e515cc395956a73e6f5f28657b6a06cd92607fe2b57626dab8ea3a617393531ede8f9ddcec7d28652c3c1db65cd9047b172096975434d9561105379'
        '4431ab17223066fe0d4e2f719a747258c8c7459feedf37682154b5b963ec55dabab9c0d6753ffca8016b79d9ed92be96281381bea6f73462bed79f39d70362e5'
        '83dd1b7616c39daf3c6b35a95d1d7aeda3ee25144b7139ac071e2bf3ecfa46b94c92a0e532c03e032f43e0ae5f8ff27534e9877f0de39b49b923602d4d6fe680'
        'cbb73931c060cb28fc42e25dd3d9bb1735f2b4816298410bae0776a2ee0f3df44f7aaf44e29a724edfbb9cf4875aaea6f449162bdd6c7c67356b3bb9bb4d2ecb'
        '3dbadb2775b8fae901140d1ef0b49025370c1dfe34df966a9e697e893fea81844a70edae0a5138f72d3a721bb8e30a63d4f93cd4761a85e0d5303e5f933997dc'
        '98c251ca930db3fea81e264a71ba01042a760ed6dee1c9912cd75f0ad153f339a524423addaf084439c7ff0a8877862be6392e0e3d07f7c759ad0abb9a1ee921'
        '9f8a4de0a246894ecef55637f6c7d13aa01b37f03a92e0b5647e0dae7e16ec3d8a3faeafd907d8455ecd1a6dfd2b59efbb8a1572aed5a7a7084812e76418abb5'
        '822dfb13f40bbde8f0df940bc2b002bc2ef3d544ca27abe7717bff17ac366afa36bcdb4132cb106dd64c7bb707a03395b7dd681ffe3eb35d494d06e80fbc6da1'
        '8d2e3012b1148a2b6fa29e1a805847a76c74d85c997baf141f30760380e4bb78b10b5cb2e7c2491333a22c338426ace920738a6165dcb5f25c64c0af2e4cfd50'
        '6138aee47dcdf5f16864e64e43462d98fcaa518eb27ce45b4166ab6f55d42a44614130209857d6c527c0e4203aa5be7c2589bc6995443c8af7886f9bb2edb0b3'
        '9baa113f8982af04ffafd26096c48c0a099e7aebeafc635c97e79fd5c70da2c348d7b40e05110d01a5f2e2c2ebf5750bab37ebe6b080b5e6c27520aec6dffc82'
        '800007316ffd19470b262b109d225952860986f45d74156a680b8297d5ffbff86f8da44390153617df16edb89693765c3825b2e14f053f966c6377109c57997a')
b2sums_x86_64=('7082013345352c95303ee87cd78bf5d93ab49ec9f270e6cb803a05cb7f9a67c554bbd260de922d6d44145fd3712b410c13d67c8f76dc2b9f4088be86aeaec835')

# https://www.kernel.org/pub/linux/kernel/v7.x/sha256sums.asc

export KBUILD_BUILD_HOST=archlinux
export KBUILD_BUILD_USER=$pkgbase
export KBUILD_BUILD_TIMESTAMP="$(date -Ru${SOURCE_DATE_EPOCH:+d @$SOURCE_DATE_EPOCH})"

prepare() {
  cd $_srcname

  echo "Setting version..."
  echo "-$pkgrel" > localversion.10-pkgrel
  echo "${pkgbase#linux}" > localversion.20-pkgname

  local src
  for src in "${source[@]}"; do
    src="${src%%::*}"
    src="${src##*/}"
    src="${src%.zst}"
    [[ $src = *.patch ]] || continue
    [[ $src = 0002-bore-fair-arch-adapt.patch ]] && continue
    [[ $src = 0004-bbr3-arch7-adapt.patch ]] && continue
    echo "Applying patch $src..."
    if [[ $src = 0001-bore-cachy.patch ]]; then
      if ! patch -Np1 < "../$src"; then
        test -s kernel/sched/fair.c.rej || exit 1
        grep -q 'sysctl_sched_tunable_scaling' kernel/sched/fair.c.rej || exit 1
        echo "Applying Arch fair.c adaptation for BORE..."
        patch -Np1 < ../0002-bore-fair-arch-adapt.patch
        rm -f kernel/sched/fair.c.rej
      fi
    elif [[ $src = 0003-bbr3-cachy.patch ]]; then
      if ! patch -Np1 < "../$src"; then
        local bbr_rejects=(
          include/linux/tcp.h.rej
          include/net/tcp.h.rej
          net/ipv4/tcp_bbr.c.rej
          net/ipv4/tcp_input.c.rej
          net/ipv4/tcp_output.c.rej
        )
        local rej
        for rej in "${bbr_rejects[@]}"; do
          test -s "$rej" || exit 1
        done
        echo "Applying Arch TCP adaptation for BBRv3..."
        patch -Np1 < ../0004-bbr3-arch7-adapt.patch
        rm -f "${bbr_rejects[@]}"
      fi
    else
      patch -Np1 < "../$src"
    fi
  done

  echo "Setting config..."
  cp ../config.$CARCH .config
  echo "Applying rgx1gen11 config..."
  while IFS= read -r rg_cfg; do
    case "$rg_cfg" in "") continue ;; esac
    if [[ "$rg_cfg" =~ ^\#\ CONFIG_([A-Za-z0-9_]+)\ is\ not\ set$ ]]; then
      scripts/config --disable "${BASH_REMATCH[1]}"
    elif [[ "$rg_cfg" =~ ^\#.*$ ]]; then
      continue
    elif [[ "$rg_cfg" =~ ^CONFIG_([A-Za-z0-9_]+)=(y|m)$ ]]; then
      if [[ "${BASH_REMATCH[2]}" == y ]]; then
        scripts/config --enable "${BASH_REMATCH[1]}"
      else
        scripts/config --module "${BASH_REMATCH[1]}"
      fi
    elif [[ "$rg_cfg" =~ ^CONFIG_([A-Za-z0-9_]+)=\"(.*)\"$ ]]; then
      scripts/config --set-str "${BASH_REMATCH[1]}" "${BASH_REMATCH[2]}"
    elif [[ "$rg_cfg" =~ ^CONFIG_([A-Za-z0-9_]+)=([0-9]+)$ ]]; then
      scripts/config --set-val "${BASH_REMATCH[1]}" "${BASH_REMATCH[2]}"
    else
      echo "unsupported rgx1gen11 config line: $rg_cfg" >&2
      exit 1
    fi
  done < ../rgx1gen11.config
  make olddefconfig
  diff -u ../config.$CARCH .config || :

  make -s kernelrelease > version
  echo "Prepared $pkgbase version $(<version)"
}

build() {
  cd $_srcname
  make all
  make -C tools/bpf/bpftool vmlinux.h feature-clang-bpf-co-re=1
}

_package() {
  pkgdesc="The $pkgdesc kernel and modules"
  depends=(
    coreutils
    initramfs
    kmod
    linux-firmware
  )
  optdepends=(
    "$pkgbase-headers: headers and scripts for building modules"
    'ddcutil: userspace DDC/CI monitor controls'
    'linux-firmware: AX211 Wi-Fi/BT and SOF firmware (also in depends)'
    'scx-scheds: to use sched-ext schedulers'
    'scx_loader: ASA router expert scheduler switching'
    'v4l2loopback-utils: utilities to control v4l2loopback devices'
    'wireless-regdb: to set the correct wireless channels of your country'
  )
  provides=(
    DDCCI-MODULE
    KSMBD-MODULE
    NTSYNC-MODULE
    V4L2LOOPBACK-MODULE
    VIRTUALBOX-GUEST-MODULES
    WIREGUARD-MODULE
  )
  replaces=(
    virtualbox-guest-modules-arch
    wireguard-arch
  )

  cd $_srcname
  local modulesdir="$pkgdir/usr/lib/modules/$(<version)"

  echo "Installing boot image..."
  # systemd expects to find the kernel here to allow hibernation
  # https://github.com/systemd/systemd/commit/edda44605f06a41fb86b7ab8128dcf99161d2344
  install -Dm644 "$(make -s image_name)" "$modulesdir/vmlinuz"

  # Used by mkinitcpio to name the kernel
  echo "$pkgbase" | install -Dm644 /dev/stdin "$modulesdir/pkgbase"

  echo "Installing modules..."
  ZSTD_CLEVEL=19 make INSTALL_MOD_PATH="$pkgdir/usr" INSTALL_MOD_STRIP=1 \
    DEPMOD=/doesnt/exist modules_install  # Suppress depmod

  install -Dm755 "$srcdir/asa-router" "$pkgdir/usr/bin/asa-router"
  install -Dm755 "$srcdir/rgx1gen11-ax211-check" "$pkgdir/usr/bin/rgx1gen11-ax211-check"
  install -Dm755 "$srcdir/rgx1gen11-memory-check" "$pkgdir/usr/bin/rgx1gen11-memory-check"
  install -Dm755 "$srcdir/rgx1gen11-pstore-check" "$pkgdir/usr/bin/rgx1gen11-pstore-check"
  install -Dm755 "$srcdir/rgx1gen11-idle-check" "$pkgdir/usr/bin/rgx1gen11-idle-check"
  install -Dm755 "$srcdir/rgx1gen11-gpu-check" "$pkgdir/usr/bin/rgx1gen11-gpu-check"
  install -Dm755 "$srcdir/rgx1gen11-sof-check" "$pkgdir/usr/bin/rgx1gen11-sof-check"
  install -Dm755 "$srcdir/rgx1gen11-nvme-check" "$pkgdir/usr/bin/rgx1gen11-nvme-check"
  install -Dm755 "$srcdir/rgx1gen11-hibernate-check" "$pkgdir/usr/bin/rgx1gen11-hibernate-check"
  install -Dm755 "$srcdir/rgx1gen11-hibernate-image-size" "$pkgdir/usr/bin/rgx1gen11-hibernate-image-size"
  install -Dm644 "$srcdir/rgx1gen11-hibernate-image-size.service" \
    "$pkgdir/usr/lib/systemd/system/rgx1gen11-hibernate-image-size.service"
  install -Dm755 "$srcdir/rgx1gen11-s0ix-preflight" "$pkgdir/usr/bin/rgx1gen11-s0ix-preflight"
  install -Dm755 "$srcdir/rgx1gen11-s0ix-tool-sync" "$pkgdir/usr/bin/rgx1gen11-s0ix-tool-sync"
  install -Dm755 "$srcdir/rgx1gen11-boot-check" "$pkgdir/usr/bin/rgx1gen11-boot-check"
  install -Dm644 "$srcdir/rgx1gen11-iwlwifi.conf" "$pkgdir/usr/lib/modprobe.d/rgx1gen11-iwlwifi.conf"
  install -Dm644 "$srcdir/rgx1gen11-btusb.conf" "$pkgdir/usr/lib/modprobe.d/rgx1gen11-btusb.conf"

  # remove build link
  rm "$modulesdir"/build
}

_package-headers() {
  pkgdesc="Headers and scripts for building modules for the $pkgdesc kernel"
  depends=(
    binutils
    glibc
    libelf
    libgcc
    openssl
    pahole
    xxhash
    zlib
    zstd
  )
  provides=(LINUX-HEADERS)

  cd $_srcname
  local builddir="$pkgdir/usr/lib/modules/$(<version)/build"

  local karch
  case $CARCH in
    x86_64) karch=x86 ;;
    *) echo "Unknown CARCH $CARCH"; exit 1 ;;
  esac

  echo "Installing build files..."
  install -Dt "$builddir" -m644 .config Makefile Module.symvers System.map \
    localversion.* version vmlinux tools/bpf/bpftool/vmlinux.h
  install -Dt "$builddir/kernel" -m644 kernel/Makefile
  install -Dt "$builddir/arch/$karch" -m644 arch/$karch/Makefile
  cp -t "$builddir" -a --no-preserve=ownership scripts
  ln -srt "$builddir" "$builddir/scripts/gdb/vmlinux-gdb.py"

  if [[ $(scripts/config -s CONFIG_HAVE_STACK_VALIDATION) = y ]]; then
    install -Dt "$builddir/tools/objtool" tools/objtool/objtool
  fi

  if [[ $(scripts/config -s CONFIG_DEBUG_INFO_BTF_MODULES) = y ]]; then
    install -Dt "$builddir/tools/bpf/resolve_btfids" tools/bpf/resolve_btfids/resolve_btfids
  fi

  echo "Installing headers..."
  cp -t "$builddir" -a --no-preserve=ownership include
  cp -t "$builddir/arch/$karch" -a --no-preserve=ownership arch/$karch/include
  install -Dt "$builddir/arch/$karch/kernel" -m644 arch/$karch/kernel/asm-offsets.s

  install -Dt "$builddir/drivers/md" -m644 drivers/md/*.h
  install -Dt "$builddir/net/mac80211" -m644 net/mac80211/*.h

  # https://bugs.archlinux.org/task/13146
  install -Dt "$builddir/drivers/media/i2c" -m644 drivers/media/i2c/msp3400-driver.h

  # https://bugs.archlinux.org/task/20402
  install -Dt "$builddir/drivers/media/usb/dvb-usb" -m644 drivers/media/usb/dvb-usb/*.h
  install -Dt "$builddir/drivers/media/dvb-frontends" -m644 drivers/media/dvb-frontends/*.h
  install -Dt "$builddir/drivers/media/tuners" -m644 drivers/media/tuners/*.h

  # https://bugs.archlinux.org/task/71392
  install -Dt "$builddir/drivers/iio/common/hid-sensors" -m644 drivers/iio/common/hid-sensors/*.h

  echo "Installing KConfig files..."
  find . -name 'Kconfig*' -exec install -Dm644 {} "$builddir/{}" \;

  echo "Installing Rust files..."
  if [[ $(scripts/config -s CONFIG_RUST) = y ]]; then
    install -Dt "$builddir/rust" -m644 rust/*.rmeta
    install -Dt "$builddir/rust" rust/*.so
  fi

  echo "Installing unstripped VDSO..."
  make INSTALL_MOD_PATH="$pkgdir/usr" vdso_install \
    link=  # Suppress build-id symlinks

  echo "Removing unneeded architectures..."
  local arch
  for arch in "$builddir"/arch/*/; do
    [[ $arch = */$karch/ ]] && continue
    echo "Removing $(basename "$arch")"
    rm -r "$arch"
  done

  echo "Removing documentation..."
  rm -r "$builddir/Documentation"

  echo "Removing broken symlinks..."
  find -L "$builddir" -type l -printf 'Removing %P\n' -delete

  echo "Removing loose objects..."
  find "$builddir" -type f -name '*.o' -printf 'Removing %P\n' -delete

  echo "Stripping build tools..."
  local file
  while read -rd '' file; do
    case "$(file -Sib "$file")" in
      application/x-sharedlib\;*)      # Libraries (.so)
        strip -v $STRIP_SHARED "$file" ;;
      application/x-archive\;*)        # Libraries (.a)
        strip -v $STRIP_STATIC "$file" ;;
      application/x-executable\;*)     # Binaries
        strip -v $STRIP_BINARIES "$file" ;;
      application/x-pie-executable\;*) # Relocatable binaries
        strip -v $STRIP_SHARED "$file" ;;
    esac
  done < <(find "$builddir" -type f -perm -u+x ! -name vmlinux -print0)

  echo "Stripping vmlinux..."
  strip -v $STRIP_STATIC "$builddir/vmlinux"

  echo "Adding symlink..."
  mkdir -p "$pkgdir/usr/src"
  ln -sr "$builddir" "$pkgdir/usr/src/$pkgbase"
}

_package-docs() {
  pkgdesc="Documentation for the $pkgdesc kernel"

  cd $_srcname
  local builddir="$pkgdir/usr/lib/modules/$(<version)/build"

  echo "Installing documentation..."
  local src dst
  while read -rd '' src; do
    dst="${src#Documentation/}"
    dst="$builddir/Documentation/${dst#output/}"
    install -Dm644 "$src" "$dst"
  done < <(find Documentation -name '.*' -prune -o ! -type d -print0)

  echo "Adding symlink..."
  mkdir -p "$pkgdir/usr/share/doc"
  ln -sr "$builddir/Documentation" "$pkgdir/usr/share/doc/$pkgbase"
}

pkgname=(
  "$pkgbase"
  "$pkgbase-headers"
)
for _p in "${pkgname[@]}"; do
  eval "package_$_p() {
    $(declare -f "_package${_p#$pkgbase}")
    _package${_p#$pkgbase}
  }"
done

# vim:set ts=8 sts=2 sw=2 et:
