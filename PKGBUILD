# Maintainer: Jan Alexander Steffens (heftig) <heftig@archlinux.org>

pkgbase=linux-rg
pkgver=7.1.8.arch1
pkgrel=5
pkgdesc='Linux kernel for linux-rg machine profiles'
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
  0011-detach-tasks-fix.patch
  0013-sched-migration-cost.patch
  0014-zen-kswapd-waiters.patch
  0015-zen-schedutil-limits.patch
  0016-cpuidle-teo-default.patch
  0018-cachy-mm-ratios.patch
  0020-cache-aware-sched.patch
  0021-mm-bulk-free-hotpaths.patch
  0022-amd-znver5-rdseed.patch
  0023-asa-workqueue-seat.patch
  0024-asa-alg1-vote.patch
  0025-asa-review-fixes.patch
  0026-asa-seat-sched.patch
  0027-asa-goal-notify-ring.patch
  0028-asa-standalone-obj.patch
  0030-asa-drop-goal-prefix.patch
  0031-asa-seat-walk-rcu.patch
  rgx1gen11.config
  rgam5terra.config
  rgSURFLat.config
  rglat5340.config
  os_linux_rg.png
  asa-router
  asa-router.service
  80-linux-rg.preset
  50-linux-rg-grokos.conf
  80-linux-rg-grokos-sessiond.conf
  rg-terra-power
  rgam5terra-memory-check
  rgam5terra-nvme-check
  rgam5terra-thermal-check
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
  rgx1gen11-live-check
  rgx1gen11-dkms-overlay-apply
  linux-rg-module-symvers
  69-linux-rg-dkms-overlays.hook
  rgx1gen11-iwlwifi.conf
  rgx1gen11-btusb.conf
  rgSURFLat-iwlwifi.conf
  rgSURFLat-btusb.conf
  rglat5340-iwlwifi.conf
  rglat5340-btusb.conf
  51-linux-rg-net-rglat5340.conf
  51-linux-rg-net-rgSURFLat.conf
  51-linux-rg-net-rgam5terra.conf
  rgam5terra-nvidia.conf
  ddcci-0.4.5-linux-7.0.patch
  rtl88xxau-r1314-linux-7.0.patch
  evdi-1.14.7-linux-7.0.patch
)
source_x86_64=(config.x86_64)
validpgpkeys=(
  ABAF11C65A2970B130ABE3C479BE3E4300411886  # Linus Torvalds
  647F28654894E3BD457199BE38DBBDC86092693E  # Greg Kroah-Hartman
  83BC8889351B5DEBBB68416EB8AC08600F108CDF  # Jan Alexander Steffens (heftig)
)
sha256sums=('ff01dcb449279d5b4cfccdb01fee639cf5ff1803f1749a77844dd33915422c49'
            'SKIP'
            '351cfb04db323bf5dd55ae8ce626650d20ba61441d202cadd8e198c6b9ef8f36'
            'SKIP'
            'f594e3a0cf55649377e09bc22e6dd5152ecafe6a96460a68036a35bba5ba932e'
            '2ce11e4224b8d75f97210b583ac5e1f4b26fcd3f3960cac3311b87ed2946a8f6'
            '55fcfaa8d9f35c9b7b61a2ffd6f147ced2e4d708e9f1336698dab0457d6f7992'
            '14ec55043d8247468aa5ccac6fde85096ff89b0182598d9d896d498acef784bd'
            '4552ccbf50e5a7c45c7f70ca8db55a444584c99c53f61ec42c74ced68ffd4658'
            'd8ae5e09265e87370655a672156bf95b9cdc3b85acc19d9b82fbf4e895efedd0'
            '1c9c4cfda09760a06927574e74e4094193d081dfb9b81e3a958379c60c17272b'
            '0fb154e8401fa57055e184b6fe922a6a81c3d5ae41e19d31548e548339839327'
            '0234dd4650400b54a5e5bcce9aeb67766e8f2e70fbf79be498ea24312ba8ea5c'
            '92c8bfd96f91ff0da27d7714360188da4e442aff1722830b1803770b9cd21a0d'
            'be700356b32a79561e4e45c12b16cc7724bebdf82b1af4e8c9a7348351e8cc9c'
            '3102018370fd41d6beee22b579349bc9420495dac7eac89175b29a2d25fb7a54'
            'f936b1e3264284b87ffe25ddbde24e1f2cbd17337576767c4d630d7271fab0b0'
            '70f173e5682f791e2c2c7974fe46cb36c3247e770de664b238a6786c20c22c9c'
            '6738c408e9b2c063da20277fd7d6f42f034dc970e6f009eb6f401268f4bf8d62'
            '4a16ea6c11d1c41d4106845f7e855fd10b734a6dd91877d091c32b2509729d7a'
            'f71db3626ffbc9be715c054ccf3127616868aa43cb2b2bf6a7b5833a26e8865a'
            'c1aa2ff3cfd18e6f024ca97ab5ee39b69d01dd15e7852e1bd3759f449272f9fc'
            'b7128076888db41d6b8049997aaefb84f8f16673c8d39ec87dbde0083618392e'
            'c1883c2e49882d06e889fab01e8e619283cad97e14beb260ada3be3f043dce76'
            '8ec566ea1fdaf34087e1ba233b9a49166f7c834d4261663b589e1a5c809156b5'
            '30b943766522f2184e51ac0870ae28ff8874095eca4775931d70cc7d592797ad'
            'd86a5aff02d8709774408db971a5d8e7a29b60ce4cbd513e72e3e50d5fea633f'
            '99d5a0e97b85085be13e3bd61eee2dc51af2a225b05c5c756774719d399d31f2'
            'fed595b88e9e10dc65fdfba8a11a1a15ba43bac05c5232b0317d0e6a0d7655bb'
            '8cd612b9b0f43b0494baed2f5847fc3db18e248a810f59a060a361304fa3163e'
            'a66bd53cd044d2d3de73ef940602f97cf5477b675f6a814a875b447d366ae681'
            '8e16033cc65915f2db21e551ffe00d45814fd176b90a85a3d1d0a9b262d69f4e'
            'f15e6b7de2991447790ce13dff2243dd30f3804baa12ac3cd3ccd17bfe82b0e3'
            'a1294cac04cb197f9dc98c85ca7d2d08ec8b329d4119a25e8f2e7cede124a7a2'
            '72a8dcd7d2fb934152a4608641abb2638dbedbf41a4ab614be227f1752384e1f'
            '74451ca1ed7c72d875ef44760171a514fe9e3885d692e1fb373195bc951f9395'
            'b8fb7602b75aed5b49315d359809b866051c125fbbd2f58ec39f34d87dd8164e'
            '9e1da6ad76ac419bc08fddd80aa0f584d66015247e59c228680aa6d510d6e338'
            '679db61df802494e7df6a86600d8c205cd49a58f7ac19097a5d0aaf66af84faf'
            '50c578bd558d3c32def5cd6d4c84d49356d83e54b00415b5584529d0a8a3b9d9'
            '7ed090e02c037129860b9042b812751b80d0e9818faad9c6109857f9423be64e'
            '2c57224feb59907decd8b9822cbda1409ef6c2a30778fbea4ac381abf978ba49'
            'da416fe965d19ab353b12b3a7d5bcec5e28fb8589f354e1ce026b03abc41e683'
            '52b000c509a2840978bd45b6cf96e890be34a34998d90e5dfc0fdf1daeefce5d'
            'ae73ca4affd8a3dd9a46d710774268e085f6bbba8462bb1a65963301f36f0579'
            'c93eef7a8fd67173d012d994ed2378ed1950beea8818fa418d099411d0de14af'
            '81f35cfa14c9883a13e75afa531f667edd27fdba0ad4925aabc57c886fee79e1'
            '1c43d5ad407881020d9d6ec8e1c1a5e23d4d0ea4eb001524e3746e5389cf7d23'
            'b844e14b2d67ae54959ed319ea02f8be260d11825474f233437f4309a213a907'
            'd8f4a69144846e4af3c7f2c66ec6c8a4d61447607fa58c52c5aa7d03ddf64365'
            '7d164766563598836978d7bfd80e26ff9ccca3eea7d476562fef66d10592a462'
            'a004b98e2f4cd1b4eec8b01ebb3f43c51c4b763fa2634cc73c9a7ba41063102c'
            'ea33da5db83296ee3313a060b746e11c184fbb3b60cfe5f5d52fe6d87523ae75'
            '99737bbda3820841aa904a95599cd126a974de262e340dca231b9b8cf8a4758c'
            '8c3aeff5ae229526346a8ad5aad5e2d8c05e1e2ad49b8d6694a422acdd5d0658'
            'd6ca16a22bb0c90e6f4f3c1b06386bc270ab41c22db64099404741ac604cac09'
            'e45756ec02180abc2fe7fc87f561d604b72dfcea3a6c535996b39d3a6fd747f0'
            '9b548bd20cf85ff19bdc986f8ebc7cb4e13bb094f85aba31616223c74b81da59'
            '923c3c53fc4d7be8d039c92671abcecee60d46a179e02ea6d8f661a35c050d19'
            '7c88d25a5b38caf3a215ebbb501038b711510f240128554b850349fee4d64c4c'
            '64ff056d5f9ae3e019a73414bddccd764f1da9841f90a69021f6237e109bdce5'
            '134551c9ab2a33011cd2cdf366e66da4cc9297011146a8abe8840f5b7a3f7408'
            '3ef3c4a79ef713154998cfecf47f66244ed81dd8d181b970f768e0a873e65e74'
            '717e3d383aa468f29ecb6a366cf45cf73bcd21d28723395770d58123cfd87755'
            '5493c4bf773dc0f274fe5d526d900556a43cadf39338a1bb0792aeb24c55ed30'
            'e65a762e14f1af909084c8f4cf591e991b1d42a300d210c8fa1e6fc644fb13a9'
            '3879b286274def79525900445c560a8584b5cff49789da04aa1b0fff41db9184'
            '198b8d371cc71d57af8bd48d944388180b335b7dc03402a7bad18e312b8ab885'
            'b386767a9c26255a692371a9ebef3f6cd4d4d74365131f281c84cd5ebc0dfde6'
            '22e1e518a94e6f0c9b60d202467c0f9244c77b0807813be4584453eb9c437224'
            'ff29e5618ea5100bd7938b0da57edcce340f9202773a9ae1f07c62c8e6fcf5d3'
            '7332851854410e619113de8ea64bc0b917ee74d7edefa807626cadbc3850a37c'
            '7d94ba2a4decc1143152e7e7699b82a14ecc23cc003b45669116f0b6946d64ca'
            '91dd3f39a7204db4dbc8c288dbf199120d4ce796f00c67cf1911ee57715e202b')
sha256sums_x86_64=('9b853f428724ae2edffd330745f47f9bcb6650b10872297686cf38f035f85134')
b2sums=('84b59e5572d91f5ea1bb603aa7691851bd9549e1bf18a6bec8e27eb8a6e2de2e33da2ad3e3aad501c793e9756e70245a16545e76b65a44ee52b33ccf5c3dd8e7'
        'SKIP'
        '308952977c15ac3ad976ff1d99d0d186814d4b03e1c8512fc3a4c0ac1ecce3f74be8f3900a7fd286492d4f930bedc089674bf713a278fa80c35413e0e6339f97'
        'SKIP'
        '9dc1a5a46d8ecf606323926f22b4ce0aaf910dc47fd9ab9b8d08d1600e0bb45109babf7098f390562d8d8456239bb44b7db13b175fe2f529b9784a603dc11fbe'
        '68a3647724b3cf56bd74739b3c67ac974b320dc372b17bcef1480d2a74576967e0d70fbbb729248f3e5bec89909dad2e3388401bd7fa131eca7ebb5888ab16ef'
        'df1ebde838b04eada2279872d8fa9452c914f521f33246782b5bde517b4d42407b5e5a7cc38db9c5ae004d72cee6fc064922552501355fe4a1931f916960ad70'
        'f80d355bd4f2875e55e3817d2853af4e5e9ee64703ec294a6d2a8244fbafce2fc152e1eee6539b1d6a2710f1148a7afe813b1aeb69a6b04f68821fa723cf1eab'
        'b4f108a878bfcebf5d765c7ef37a96ef4e76894c4453595aaca7a200dd65234572bf95b7bec8640af2c2f97534230e12c06a6330e853134932e22625308b3124'
        'b13e277497e8d688beb8e69bf8eac9e4b0f760d927a4c02b4b0fe80c8be43022dc3e8e5b68377827aca40fd03eefd648dc638e51024b837a9dd438448cbfa0a1'
        '1e03198bd2c832238c5d4dfc0fa742ea32db994f4a19bfde84745d40d77c85476aee1832b45d153d071fb124e967423fac112c1f8b4da38ac90458fd3e023493'
        'de2717075b6af543f888d2a6604180f0d256fa3abe0109efeaf876939ad186195d57b667dc5a757d97c4fdc77a1fca4f4499c144a82793d9cb7bc00db0ef5412'
        'c273056194360156e1ec6bf20e0ae1ab2d2857e52aaafb92421619891f3ea13b508cb2f16dabc4baa8da6d6318066118d33dadbcfff8f69b4bb6f094a31fff61'
        'c9ff8674f26e0bd49a1cbecbd7ef4ab76507ecca4d5d3e085fdbadf6c809fb652fa209395684e5042b28532cc723ac11083d48414aa7805536c199abfef33797'
        '43092dc75bf584705b4075be1a53a85833420c7e3a7ea55b02e9add1a33160f06bf497792a4f5dcd11be2e99eb5fa3a91f13ea79bb1873434350ac975dec2b72'
        '08e550a84c84df1059225a0096e5d829a223c695511464b753614c0102b60ba59f7960a35535459822a56ef434c89ee54601e813c0cf3d4985ea05f1e31e4561'
        '8ca24572f81b16fbb1138b7b4681e34c107b9e77bf031e69884a4abb0216aa666cf24215e5235276b15e335e397a3a42645103c1cb515f84f69172a145dddc85'
        'd15aab2d06223b62ba4a675f626539e6b75632cb5ba6820ba71fd2298dd9859eb4d83d614e44504e75f1aae4f6a78f1d8ef9f4f1eb135f79a5cd688fc4ce1253'
        'ac381c060eeb5f39aa3432ddd84485db0a209fa476b947500dd04b54bda5ba843601a99fc8ca3d0e9f201ac8a9d0a4f390f681e92074e43cf3de8d36092f980f'
        '92ee3cc4563c2eab361f02d9a7662bdf9a340a9f57cea58f8b9ba56c815772bc1529f3cc76c81aaaec6cd5f01a540db84f4f79dbd1f0840fa501c4ea141aedc0'
        '4f344c4eff4acb548f75513d04eae88377444f2da3eee7f92f2fc9b216d66d04b90d612de81dee151285815eeadd13530087d69cb45c0064cf3e0fcf94319852'
        'e4adc5f4d70c0a35472e5a1383a9cccb142dff0844cfe9000a4870c9633b7b9c57ea28c12f305c14e9e65a5d7ceb27f99edfb8d42f3434cc65f0142bf64bd862'
        '426294e76da1f86d013c81ef75abd675a090560959e1a686f808ae86099b577fff8b03e7b47c9f2cadb37e6795048fb0f55b0e083e2a49859de7a53ff981d511'
        '5c7f055cfee92d2eacedd2a6453c6050b7cafe14612d46cc7dc7a185030c7349602c5a10eb6e5c5972d4b22a7dc5da43593a1ec79700f826f7a5963aa3497490'
        '8621501c8797abb33b632f23f0a6f2f6488a91d1a922f56b8699172b24a19cd26a72ef700cbdf3132dc65d8d010313ddd92a1842c3f2a7400b47fac324ddfed5'
        'd45d35a73b72a054909eefdbf951a49d538c6db33b33533b1b91fbdc7704218e7a007aea4d5c30063b7c3ca666fd048c08aca0af6a5adb36a2663dbdf96b95dc'
        '4adcf704200aeeec81461fe4709e3388667195186e4ae5572e24bfbeb767f0ec8b4596e0696192b119251e11e95933e36fb3b1e030bcb5b7953ea843d28c540d'
        '4491aca57fb2c886ba37f44be1ed2fe9992ff3d5e02cb03fc3b97b59aad7a62409d722a7d8a3cafb9ffb45dc40de78b8bd8a4cf0e67e5eeea273f8d3b2dda1fe'
        '94c341663fe693e6ddf40e33cb3f7ed018d7f62f28726f25803ffb1af3c5cbaf93b56a28babfc8c220683fccfbb3e68910c268cc39be606c042bee89531a9618'
        'efda28c310e2d23a196705bba3653b6f3bc10ca2cb1edccdac7b8bb1b6341f516280ef4b1e1eae095cc30d3586edfe72502c1285b0aeb2bd7e3bb369c496a4ef'
        'c5d76813c22a5d1088a81766af82143370a467045cae428cbe44d614d60a9c531660e12da1d62b2e76a12bf2618eb112dbec8cf68fbf88aa4e5b5c63c04a23cf'
        '9966fc41caac7b6ec06fb6c2b1ef264c12895eabf64aa48d25550d045afd99c6cc84eae0e0a30581e55b1ac7fa47fdc5512047a0bd3921d6708bc527cb54c8f7'
        '5edaa0269d7ac78030f393e6f952f4cecacaff11fdffd4a939b772c56cdfbadd3a92ed045d1d5e8b399205af2ce2a6319138ca56cbc7ad300c2e09fddbc84694'
        '8efccb2466e9ccb16190d354b040314722ec35f051e631af466fcb66fff1d2436add8b4b4fcdab6f43f6b8dec25733065db7a0559337d9a869745ce3a804d9a9'
        '064a62fc3b63c501cf369e65fb0d9e89d1e87348f373051f37c3ed23630fd77b2b90efc351c2a37663be18d488e623b19e3f25b4922343ab4cfe937224938d93'
        '6b9ea66c172ae82926bf5bd18fbed6f6a246fa3cc6104599d88709dc634a9e9cdd861cbfcfc86820fe687d80191de2427fa8b48dad11579b2b8335ceb59e2808'
        '204eb91154ea27a891941a6ce71e6fff2ebf84e815d2ae3bcd03a188759ad4782b6dfb69295558c7598ab0b6c93bc6c739b86e4ae68921707e98cfae2a338a26'
        '6b91287d917c2b192712d90548010ddcadad4c0b3c927916827a44d955f797eadef27daf806053570ae59201558199599a0aaffe93a353422d6e3a5d57211437'
        '5de509332b5706b384762321e37d4129e444fe3beb183ae772efea1b22455083c765e107ca74410eb0f282346d87c98ecb1a1b997ca5a7afd339fe6ec1811e5f'
        '268f2f0274be974e5deb544a9c014477afd89974ae1bdb25445718c71c4033b324d89663badb0e718e040b7feb509d170da7eeabcb9016391a92feafae61de33'
        '46b138b363e9a399b9ec9da510395f39399c25342962b61f97aa5da97cd70dfe30c20f7f5c39072dcf6038b94e30cb142c3dd86c08df53c8ea2466f238103eb1'
        '8990e9a454aed0459a1a1dd24e8fe8b5cd1b30cb3d2ded11e86c0a7a1e57e828c058541ec461d0ae43261a846e17ba29688a3e7433f98fa9df4b357dec807f4a'
        '8ccd16659f42098f8c7952346c8091ff508e3f2254f64af68ce7065f4d8efc87f3dacfc9048240b95252978291c14dff13c18bbc1a3d80060c5582ddb47249ae'
        '23404ef0e006662f6b5cc650e434da71060b6172226a7d5add0389af00ccf0c0b43bf7dfb30f4be52463e3c6780dc568fe70d0ecaff0977fb2c473137a127645'
        '9025bb521840b05518bb39fff120cc6ba8ee90b09886631cf9868a5731151b064fb2c8ac22ad910eeb1e32437785df97a3e2a3bd43581c314a6ff34bebca85e6'
        '07cded2cc1fca1953b9c19b3664a1d0eac52b964cee2df683698a79e246eb03de7e4cd646f64187f21ef4da9bc02211496722d71b961347d8b7c85b34c52dca8'
        'c0efa28a08c225f90e40858319760ee1b6ebcfcaa8241ba996b5df61cd2e457e4dabe35dd4a9b49ed0243c1789902de8d82e4e73e4a02efbd89efcde8d3916d3'
        '43177b575c96edc140895e6b2ad11d01183cc67a7d26a8f52a9a62a6aff64c2f5d41077465fd5c4e0c37967ba5430107e84f909d88c6fb5b9dee82a661368ed1'
        '4431ab17223066fe0d4e2f719a747258c8c7459feedf37682154b5b963ec55dabab9c0d6753ffca8016b79d9ed92be96281381bea6f73462bed79f39d70362e5'
        '971b499751c5808a6bbf06c80d5f8f5797b0c01d8955745c6b3efc6315c107a3df33829318e972d5a1bb94af16fa7cad3d869436c81725e9d14a33e4de24a642'
        '30486d3e8653f063512764e9dd6a49e5b133e94b25164f9a0bb4f4701aeeee04b55db1148c05165e114559fa6eb9c08b45398ca15a0e9c624ac2c9102df59c23'
        '3dbadb2775b8fae901140d1ef0b49025370c1dfe34df966a9e697e893fea81844a70edae0a5138f72d3a721bb8e30a63d4f93cd4761a85e0d5303e5f933997dc'
        '98c251ca930db3fea81e264a71ba01042a760ed6dee1c9912cd75f0ad153f339a524423addaf084439c7ff0a8877862be6392e0e3d07f7c759ad0abb9a1ee921'
        '9f8a4de0a246894ecef55637f6c7d13aa01b37f03a92e0b5647e0dae7e16ec3d8a3faeafd907d8455ecd1a6dfd2b59efbb8a1572aed5a7a7084812e76418abb5'
        'b471180bd622c0a6069b19505b29ac95bfad0f43ca01f5bed5765c11830a8ef75f93b5506b198a16422fe3c8263fc31150a067a336bcbf92224f846ed121614d'
        '94dbc482b57cb1c1ceb7469a518af49bf684612e5f77ac31ed83b61633b21bcb29c03c0ac8f79a8629c38b0130be81b8e9909a35f5eccdbc4fc832d7cd57b108'
        '343db7ebfff2ebc96f42b0f3658c6333378ea42215da61342d8e76d0958b0bf300323dcc6e888262a167f77aa36e92d3e01614e6d6a0e5e718e4e41c0140f591'
        '8f9c9227e8a7efd60ba78317ab85952841124b564b5120061fb085769cddebaf21259e711d2cc1160465e6866b409d35d460cb75a5b727e7a0b140888baf07b5'
        '11a2a6f73b5b4f33f5901db372444832061e450efbe5123cca67751b2cbc934504cb4f1824acb14df4fe586d8c8da714b22e26ce2213f974a970625d114e729b'
        '2d04ddc4f81eb7a5ccd4be176ef2ac1e8f9173efcac187bb35b11afb5cead37f1b3c9ff12f50150ec52bafbfa31fb842ee6082fb35db450e4fa2346b98f73dc7'
        '25ac8b6b62138b8be097fcdf23240fb6f0ffa2c6248fa5b2feca9d6913883fee232ca0c00c1154e084567032312a9e1699d12230999fa0a0fe827f1795d473f6'
        '9baa113f8982af04ffafd26096c48c0a099e7aebeafc635c97e79fd5c70da2c348d7b40e05110d01a5f2e2c2ebf5750bab37ebe6b080b5e6c27520aec6dffc82'
        '800007316ffd19470b262b109d225952860986f45d74156a680b8297d5ffbff86f8da44390153617df16edb89693765c3825b2e14f053f966c6377109c57997a'
        'cdcdec4d9ab47632fec84dcafbd128181af5abda7e36c906edd995d25053f2244a6ffebfb97ebecf8f217dfcdf3a6e346fa111f177c23b463504125cb0535f98'
        'ebc6c13c18776dc5d366713a0e6fec82f094ecfef8b95eca5a5db842fd710db9fb7ff8b4e276dfb9adace6b343e15b5f342d9eda25b51fb9408acd44f839e835'
        '5dc0334264fbdbf520b0901acb7d158e7d94b9e50cc0ff548822afb3bf08a3e6277c3487406193742b23a2b0da6ad7193b6ee8720a2a5451dca35b9fcfaaa5f6'
        'c8209c046435a5ae61d84f19da49fbb2301f81d72c89b4346e7378ad60f523ffb4d16c61272d5e48d141cbedf4f8a30bbb5e4bb17266453a3b56facd4bbeaf15'
        '9d9e6c5de426e1c6d6408f38538d352964e0eaa9a05e9d2f67dd9f3663c5d48df2d294c1f15b2e2e41ab1a0ce0ae507ce8a629c5bbcc223fc7241d87598045b4'
        '84551a56f6fff993b031fc83d7c23cfdd6d047c411859ce333c093f8aa5ccfcc14b0bb8d97eaabf5990b83d1c643a1b4741fe191c9fed0768d6bca583fcf9d33'
        'd380f5180ac93f13d55b920f54be62622ba4e08b65666a1b0753c053c384596ff65530ca576bec23636d88693364bb0d3d3c9c56802be7ffadec5974883f1b2e'
        'eff9fd360fcf2299deea61132a10818f7a674811fbe74848bcb405773e97e8dee5db2aa1ad1b2681504ea0a6e78e10e209522f42754ea7f84294832b12330c16'
        '687e4c74aba0e69a5f6a8f8989d62ca38cceaadd5100f5c7773c010c84efece4968ffed9e7cf429571ee934c09f5fc5cc7835771ee62e7cdd5998561427c8e70'
        '303599598195026b76c1d8b6a6456a4f2b2ade01026e93c96ae4bc968eee4bea015b7fe0e4180d0a250f98828d52b42b4f4a4d47d3811ce735da9dc0bac3d445'
        '7b9c5e5e3d3393d2ae1cc2c2cd55c1896c5e6ecc0c7a71178ebb297f9426b11cb7c5f98efc610e09cbaf808ea172375242d38d00bad81a7c08968f499e3869a6')
b2sums_x86_64=('b10d80423aa3eb65e2046bf5b1998f9a7bdbc97494c6881881f50ffcdb5fe2e242782f59dbb6402cd77ce64b988dbf295fd9fa54f20180c76fbe88b82e1dbc9d')

# https://www.kernel.org/pub/linux/kernel/v7.x/sha256sums.asc

export KBUILD_BUILD_HOST=archlinux
export KBUILD_BUILD_USER=$pkgbase
export KBUILD_BUILD_TIMESTAMP="$(date -Ru${SOURCE_DATE_EPOCH:+d @$SOURCE_DATE_EPOCH})"

_linux_rg_apply_path_remap() {
  local map_path
  local map_paths=(
    "$PWD"
    "$srcdir"
    "$startdir"
  )
  for map_path in "${map_paths[@]}"; do
    [[ -n $map_path ]] || continue
    export KCPPFLAGS="${KCPPFLAGS:+$KCPPFLAGS }-fmacro-prefix-map=$map_path=."
    export KCFLAGS="${KCFLAGS:+$KCFLAGS }-fdebug-prefix-map=$map_path=. -ffile-prefix-map=$map_path=. -fmacro-prefix-map=$map_path=."
    export KRUSTFLAGS="${KRUSTFLAGS:+$KRUSTFLAGS }--remap-path-prefix=$map_path=."
  done
}

prepare() {
  cd $_srcname

  echo "Setting version..."
  echo "-$pkgrel" > localversion.10-pkgrel
  echo "${pkgbase#linux}" > localversion.20-pkgname
  local linux_rg_profile=${LINUX_RG_PROFILE:-rgx1gen11}
  case "$linux_rg_profile" in
    rgx1gen11|rgam5terra|rgSURFLat|rglat5340) ;;
    *) echo "unsupported linux-rg profile: $linux_rg_profile" >&2; exit 1 ;;
  esac
  echo "Using linux-rg profile: $linux_rg_profile"

  local src
  for src in "${source[@]}"; do
    src="${src%%::*}"
    src="${src##*/}"
    src="${src%.zst}"
    [[ $src = *.patch ]] || continue
    [[ $src = 0002-bore-fair-arch-adapt.patch ]] && continue
    [[ $src = 0004-bbr3-arch7-adapt.patch ]] && continue
    [[ $src = 0010-cachy-hotpath-inline.patch ]] && continue
    [[ $src = 0012-sched-ext-smt-idle.patch ]] && continue
    [[ $src = 0017-bbr3-tcp-prototype.patch ]] && continue
    [[ $src = 0019-mglru-devtree-adapt.patch ]] && continue
    [[ $src = ddcci-0.4.5-linux-7.0.patch ]] && continue
    [[ $src = rtl88xxau-r1314-linux-7.0.patch ]] && continue
    [[ $src = evdi-1.14.7-linux-7.0.patch ]] && continue
    [[ $src = 0022-amd-znver5-rdseed.patch && $linux_rg_profile != rgam5terra ]] && continue
    echo "Applying patch $src..."
    if [[ $src = 0001-bore-cachy.patch ]]; then
      if ! patch -Np1 < "../$src"; then
        test -s kernel/sched/fair.c.rej || exit 1
        grep -q 'sysctl_sched_tunable_scaling' kernel/sched/fair.c.rej || exit 1
        echo "Applying Arch fair.c adaptation for BORE..."
        patch -Np1 < ../0002-bore-fair-arch-adapt.patch
        rm -f kernel/sched/fair.c.rej kernel/fork.c.rej
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
  local localmodconfig=${LINUX_RG_LOCALMODCONFIG:-1}
  local lsmod_snapshot="$startdir/$linux_rg_profile.lsmod"
  if [[ $localmodconfig = 1 && -s $lsmod_snapshot ]]; then
    echo "Applying $linux_rg_profile module allowlist..."
    make LSMOD="$lsmod_snapshot" localmodconfig
  fi
  echo "Applying $linux_rg_profile config..."
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
      echo "unsupported $linux_rg_profile config line: $rg_cfg" >&2
      exit 1
    fi
  done < "../$linux_rg_profile.config"
  make olddefconfig
  if ! grep -q '^CONFIG_SOCK_CGROUP_DATA=y' .config; then
    echo "CONFIG_SOCK_CGROUP_DATA dropped after olddefconfig" >&2
    exit 1
  fi
  if ! grep -qE '^CONFIG_NFT_SOCKET=[ym]$' .config; then
    echo "CONFIG_NFT_SOCKET dropped after olddefconfig" >&2
    exit 1
  fi
  if ! grep -qE '^CONFIG_NETFILTER_XT_MATCH_CGROUP=[ym]$' .config; then
    echo "CONFIG_NETFILTER_XT_MATCH_CGROUP dropped after olddefconfig" >&2
    exit 1
  fi
  if ! grep -qE '^CONFIG_CRYPTO_CRYPTD=[ym]$' .config; then
    echo "CONFIG_CRYPTO_CRYPTD dropped after olddefconfig" >&2
    exit 1
  fi
  # The routing helpers' network stack. A snapshot taken without the tunnels
  # and policy rules loaded lets localmodconfig drop these; refuse to build a
  # kernel whose network planes would come up dead.
  local rg_net_opt
  for rg_net_opt in NF_TABLES_INET NF_CONNTRACK NFT_COMPAT NFT_CT NFT_REJECT NFT_REJECT_INET \
      NFT_FIB_INET NFT_NAT NFT_MASQ NETFILTER_XT_MATCH_COMMENT NETFILTER_XT_MATCH_OWNER \
      NETFILTER_XT_MATCH_ADDRTYPE NETFILTER_XT_MATCH_CONNTRACK NET_CLS_CGROUP WIREGUARD \
      VETH TUN IP_MULTIPLE_TABLES IPV6_MULTIPLE_TABLES; do
    if ! grep -qE "^CONFIG_${rg_net_opt}=[ym]$" .config; then
      echo "CONFIG_${rg_net_opt} dropped after olddefconfig" >&2
      exit 1
    fi
  done
  local module_count module_budget
  module_count=$(grep -c '^CONFIG_.*=m$' .config || :)
  case "$linux_rg_profile" in
    rgx1gen11|rgSURFLat|rglat5340) module_budget=${LINUX_RG_MODULE_BUDGET:-1500} ;;
    *) module_budget=${LINUX_RG_MODULE_BUDGET:-0} ;;
  esac
  if (( module_budget > 0 )); then
    echo "$linux_rg_profile module config count: $module_count / $module_budget"
    if (( module_count > module_budget )); then
      echo "$linux_rg_profile module config count exceeds budget" >&2
      echo "set LINUX_RG_MODULE_BUDGET to an explicit higher value for broad builds" >&2
      exit 1
    fi
  fi
  diff -u ../config.$CARCH .config || :

  make -s kernelrelease > version
  echo "Prepared $pkgbase version $(<version)"
}

build() {
  cd $_srcname
  _linux_rg_apply_path_remap
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
    patch
  )
  optdepends=(
    "$pkgbase-headers: headers and scripts for building modules"
    'ddcutil: userspace DDC/CI monitor controls'
    'dkms: rebuild external module overlays for linux-rg'
    'linux-firmware: AX211 Wi-Fi/BT and SOF firmware (also in depends)'
    'scx-scheds: to use sched-ext schedulers'
    'scx-tools: ASA router expert scheduler switching with scx_loader'
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
  install -Dm644 "$srcdir/rgx1gen11.config" "$pkgdir/usr/share/linux-rg/profiles/rgx1gen11.config"
  install -Dm644 "$srcdir/rgam5terra.config" "$pkgdir/usr/share/linux-rg/profiles/rgam5terra.config"
  install -Dm644 "$srcdir/rgSURFLat.config" "$pkgdir/usr/share/linux-rg/profiles/rgSURFLat.config"
  install -Dm644 "$srcdir/rglat5340.config" "$pkgdir/usr/share/linux-rg/profiles/rglat5340.config"
  install -Dm644 "$srcdir/os_linux_rg.png" "$pkgdir/usr/share/linux-rg/refind/os_linux_rg.png"
  echo "$pkgbase" | install -Dm644 /dev/stdin "$modulesdir/pkgbase"

  echo "Installing modules..."
  ZSTD_CLEVEL=19 make INSTALL_MOD_PATH="$pkgdir/usr" INSTALL_MOD_STRIP=1 \
    DEPMOD=/usr/bin/true modules_install  # Pacman hooks regenerate module indices.

  install -Dm755 "$srcdir/asa-router" "$pkgdir/usr/bin/asa-router"
  install -Dm644 "$srcdir/asa-router.service" \
    "$pkgdir/usr/lib/systemd/system/asa-router.service"
  install -Dm644 "$srcdir/80-linux-rg.preset" \
    "$pkgdir/usr/lib/systemd/system-preset/80-linux-rg.preset"
  install -Dm644 "$srcdir/50-linux-rg-grokos.conf" \
    "$pkgdir/usr/lib/sysctl.d/50-linux-rg-grokos.conf"
  local linux_rg_net_profile=${LINUX_RG_PROFILE:-rgx1gen11}
  case "$linux_rg_net_profile" in
    rglat5340|rgSURFLat|rgam5terra)
      install -Dm644 "$srcdir/51-linux-rg-net-${linux_rg_net_profile}.conf" \
        "$pkgdir/usr/lib/sysctl.d/51-linux-rg-net-${linux_rg_net_profile}.conf"
      ;;
  esac
  install -Dm644 "$srcdir/51-linux-rg-net-rglat5340.conf" \
    "$pkgdir/usr/share/linux-rg/net/51-linux-rg-net-rglat5340.conf"
  install -Dm644 "$srcdir/51-linux-rg-net-rgSURFLat.conf" \
    "$pkgdir/usr/share/linux-rg/net/51-linux-rg-net-rgSURFLat.conf"
  install -Dm644 "$srcdir/51-linux-rg-net-rgam5terra.conf" \
    "$pkgdir/usr/share/linux-rg/net/51-linux-rg-net-rgam5terra.conf"
  install -Dm644 "$srcdir/80-linux-rg-grokos-sessiond.conf" \
    "$pkgdir/usr/lib/systemd/user/grokos-sessiond.service.d/linux-rg.conf"
  install -Dm755 "$startdir/scripts/linux-rg-grokos-sessiond-check" \
    "$pkgdir/usr/bin/linux-rg-grokos-sessiond-check"
  install -Dm755 "$startdir/scripts/linux-rg-grokos-seat-check" \
    "$pkgdir/usr/bin/linux-rg-grokos-seat-check"
  install -Dm755 "$startdir/scripts/linux-rg-criu-check" \
    "$pkgdir/usr/bin/linux-rg-criu-check"
  install -Dm755 "$startdir/scripts/rgx1gen11-network-policy-check" \
    "$pkgdir/usr/bin/rgx1gen11-network-policy-check"
  install -Dm755 "$startdir/scripts/linux-rg-grokos-tune-check" \
    "$pkgdir/usr/bin/linux-rg-grokos-tune-check"
  install -Dm755 "$startdir/scripts/linux-rg-asa-router-check" \
    "$pkgdir/usr/bin/linux-rg-asa-router-check"
  install -Dm755 "$srcdir/rg-terra-power" "$pkgdir/usr/bin/rg-terra-power"
  install -Dm755 "$srcdir/rgam5terra-memory-check" "$pkgdir/usr/bin/rgam5terra-memory-check"
  install -Dm755 "$srcdir/rgam5terra-nvme-check" "$pkgdir/usr/bin/rgam5terra-nvme-check"
  install -Dm755 "$srcdir/rgam5terra-thermal-check" "$pkgdir/usr/bin/rgam5terra-thermal-check"
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
  install -Dm755 "$srcdir/rgx1gen11-live-check" "$pkgdir/usr/bin/rgx1gen11-live-check"
  install -Dm755 "$srcdir/rgx1gen11-dkms-overlay-apply" "$pkgdir/usr/bin/rgx1gen11-dkms-overlay-apply"
  install -Dm755 "$srcdir/linux-rg-module-symvers" "$pkgdir/usr/bin/linux-rg-module-symvers"
  install -Dm644 "$srcdir/69-linux-rg-dkms-overlays.hook" \
    "$pkgdir/usr/share/libalpm/hooks/69-linux-rg-dkms-overlays.hook"
  install -Dm644 "$srcdir/rgx1gen11-iwlwifi.conf" "$pkgdir/usr/lib/modprobe.d/rgx1gen11-iwlwifi.conf"
  install -Dm644 "$srcdir/rgx1gen11-btusb.conf" "$pkgdir/usr/lib/modprobe.d/rgx1gen11-btusb.conf"
  install -Dm644 "$srcdir/rgSURFLat-iwlwifi.conf" "$pkgdir/usr/lib/modprobe.d/rgSURFLat-iwlwifi.conf"
  install -Dm644 "$srcdir/rgSURFLat-btusb.conf" "$pkgdir/usr/lib/modprobe.d/rgSURFLat-btusb.conf"
  install -Dm644 "$srcdir/rglat5340-iwlwifi.conf" "$pkgdir/usr/lib/modprobe.d/rglat5340-iwlwifi.conf"
  install -Dm644 "$srcdir/rglat5340-btusb.conf" "$pkgdir/usr/lib/modprobe.d/rglat5340-btusb.conf"
  install -Dm644 "$srcdir/rgam5terra-nvidia.conf" "$pkgdir/usr/lib/modprobe.d/rgam5terra-nvidia.conf"
  install -Dm644 "$srcdir/ddcci-0.4.5-linux-7.0.patch" \
    "$pkgdir/usr/share/linux-rg/dkms-overlays/ddcci-0.4.5-linux-7.0.patch"
  install -Dm644 "$srcdir/rtl88xxau-r1314-linux-7.0.patch" \
    "$pkgdir/usr/share/linux-rg/dkms-overlays/rtl88xxau-r1314-linux-7.0.patch"
  install -Dm644 "$srcdir/evdi-1.14.7-linux-7.0.patch" \
    "$pkgdir/usr/share/linux-rg/dkms-overlays/evdi-1.14.7-linux-7.0.patch"

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
  _linux_rg_apply_path_remap
  local builddir="$pkgdir/usr/lib/modules/$(<version)/build"

  local karch
  case $CARCH in
    x86_64) karch=x86 ;;
    *) echo "Unknown CARCH $CARCH"; exit 1 ;;
  esac

  echo "Installing build files..."
  install -Dt "$builddir" -m644 .config Makefile Module.symvers System.map \
    localversion.* version vmlinux tools/bpf/bpftool/vmlinux.h

  echo "Completing Module.symvers from module export tables..."
  "$srcdir/linux-rg-module-symvers" "$PWD" > "$builddir/Module.symvers.modules"
  awk '!seen[$2]++' "$builddir/Module.symvers" "$builddir/Module.symvers.modules" \
    > "$builddir/Module.symvers.merged"
  mv "$builddir/Module.symvers.merged" "$builddir/Module.symvers"
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
