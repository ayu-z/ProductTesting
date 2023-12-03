ping 192.168.10.2;tftpb openwrt-ipq6018-u-boot.mbn;sf probe;sf erase 0x5c0000 +0xa0000;sf write 0x44000000 0x5c0000 0xa0000;tftpb 2022-04-28-x5.ubi;flash rootfs

tftpb norplusnand-ipq6018_64-single.img;imgaddr=$fileaddr;source $imgaddr:script


setenv bootcmd 'bootm 0x9f050000';saveenv;tftpboot 2022-04-19-x2.bin;erase 0x9f0500000 +0xfa0000;cp.b 0x80800000 0x9F050000 0xA8030A
