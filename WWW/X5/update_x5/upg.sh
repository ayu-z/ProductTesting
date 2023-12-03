#!/bin/sh 

#update nor flash to support kernel5.4 firmware, old nor flash not support kernel 5.4 firmware
for i in `seq 0 14`
do 
   mtd erase /dev/mtd$i
done
if ls /tmp/x5.flash.bin;then
   dd if=/tmp/x5.flash.bin of=/dev/mtd0 bs=64k skip=0 count=12
   dd if=/tmp/x5.flash.bin of=/dev/mtd1 bs=64k skip=12 count=1
   dd if=/tmp/x5.flash.bin of=/dev/mtd2 bs=64k skip=13 count=2
   dd if=/tmp/x5.flash.bin of=/dev/mtd3 bs=64k skip=15 count=2 
   dd if=/tmp/x5.flash.bin of=/dev/mtd4 bs=64k skip=17 count=26
   dd if=/tmp/x5.flash.bin of=/dev/mtd5 bs=64k skip=43 count=26
   dd if=/tmp/x5.flash.bin of=/dev/mtd6 bs=64k skip=69 count=1
   dd if=/tmp/x5.flash.bin of=/dev/mtd7 bs=64k skip=70 count=1
   dd if=/tmp/x5.flash.bin of=/dev/mtd8 bs=64k skip=71 count=4
   dd if=/tmp/x5.flash.bin of=/dev/mtd9 bs=64k skip=75 count=4
   dd if=/tmp/x5.flash.bin of=/dev/mtd10 bs=64k skip=79 count=1
   dd if=/tmp/x5.flash.bin of=/dev/mtd11 bs=64k skip=80 count=1
   dd if=/tmp/x5.flash.bin of=/dev/mtd12 bs=64k skip=81 count=1
   dd if=/tmp/12.0-ipq6018-u-boot.mbn of=/dev/mtd13 
else
   echo "no flash file"
   return 1
fi


# update ubi firmware
if ls /tmp/firmware.bin;then
    source /lib/functions.sh
    mtdnum=`find_mtd_index rootfs`
    ubidetach -f -p /dev/mtd$mtdnum
    ubiformat /dev/mtd$mtdnum -y -f /tmp/firmware.bin
    sleep 5
    reboot
else
   echo "no upgrade file"
   return 1
fi