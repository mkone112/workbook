
parted /dev/sdX
(parted) mkpart ESP fat32 1MiB 513MiB
(parted) set 1 boot on