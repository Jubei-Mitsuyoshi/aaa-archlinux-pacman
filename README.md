aaa-archlinux-pacman
====================

archlinux pacman packaged for debian


after install instructions

uncheck one mirror in /ets/pacman.d/mirrorlist



/etc/pacman.conf should be 

[options]
HoldPkg     = pacman glibc
SyncFirst   = pacman
Architecture = auto
CheckSpace
SigLevel = Never

[testing]
#SigLevel = PackageRequired
Include = /etc/pacman.d/mirrorlist

[core]
#SigLevel = PackageRequired
Include = /etc/pacman.d/mirrorlist

[extra]
#SigLevel = PackageOptional
Include = /etc/pacman.d/mirrorlist

[community-testing]
#SigLevel = PackageRequired
Include = /etc/pacman.d/mirrorlist

[community]
#SigLevel = PackageOptional
Include = /etc/pacman.d/mirrorlist

[multilib-testing]
#SigLevel = PackageRequired
Include = /etc/pacman.d/mirrorlist

[multilib]
#SigLevel = PackageOptional
Include = /etc/pacman.d/mirrorlist


then


pacman-key --init
pacman -Sy archlinux-keyring
pacman-key --populate archlinux
pacman -Sy

/root/git/github/aaa-arch-install-scripts/README.md


STATUS: packaged running
