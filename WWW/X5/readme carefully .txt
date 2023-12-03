1.upgrade firmware by scp and shell command:
    a. scp the firmware(2022-03-24-x5.bin and upg.sh and x5.flash.bin ) to 
root@192.168.11.1:/tmp/ by winscp or other scp tool.
    b. login to ssh root@192.168.11.1 command line by putty or other ssh tool.
    c. below is the command lines:

source /lib/upgrade/common.sh
install_bin /usr/bin/seq
chmod +x /tmp/upg.sh
run_ramfs ". /lib/functions.sh; sh /tmp/upg.sh"



2. upgrade firmware by uboot/serial/tftpb:
    a. set static ip 192.168.10.2 mask 255.255.255.0 on windows 
    b. connect the router to windows pc by RJ45 cable , then open tftpd.exe on windows
    c. connect usb to uart(GND/TX/RX) cable to windows
    d. open the serial terminal(for example MobaXterm) at 115200bps/8N1, power on the  x5 router 
    e. keep type any key in the serial terminal, then we get in uboot mode.
    f. You can check the flash struction by "smeminfo" command.
    g. type "tftpb openwrt-ipq60xx-generic-ylx_x5-squashfs-nand-factory.ubi" upload the firmware.
    h. type "flash rootfs" to upgrade the firmware.
    i. type "reset" to restart the system.

  if the firmware not work(keeping restart when enter kernel), we need to re-flash  the whole nor flash to support kernel 5.4 firmware:
  Below is the steps:
    a. type "tftpb   x5.flash.bin" to upload the flash bin CONFIG_FIX_EARLYCON_MEM
    b. type "sf probe; sf erase 0x0 +0x660000" to erase the flash
    c. type "sf write 0x44000000 0x0 0x660000" to flash the nor flash.
    d. type "reset" to restart the system.