#!/bin/sh

. /lib/functions.sh
. /lib/functions/system.sh

xor() {
        local val
        local ret="0x$1"
        local retlen=${#1}

        shift
        while [ -n "$1" ]; do
                val="0x$1"
                ret=$((ret ^ val))
                shift
        done

        printf "%0${retlen}x" "$ret"
}

change_mac_withCRC() {
	local mac=$1
	local mac_offset=$2
	local chksum_offset=$3
    local target=/tmp/art.bin
	local xor_mac
	local xor_fw_mac
	local xor_fw_chksum

	xor_mac=${mac//:/}
	mac=${mac//:/}
	xor_mac="${xor_mac:0:4} ${xor_mac:4:4} ${xor_mac:8:4}"

	xor_fw_mac=$(hexdump -v -n 6 -s $mac_offset -e '/1 "%02x"' $target)
	xor_fw_mac="${xor_fw_mac:0:4} ${xor_fw_mac:4:4} ${xor_fw_mac:8:4}"

	xor_fw_chksum=$(hexdump -v -n 2 -s $chksum_offset -e '/1 "%02x"' $target)
	xor_fw_chksum=$(xor $xor_fw_chksum $xor_fw_mac $xor_mac)

	printf "%b" "\x${xor_fw_chksum:0:2}\x${xor_fw_chksum:2:2}" | \
		dd of=$target conv=notrunc bs=1 seek=$chksum_offset count=2

    printf "%b" "\x${mac:0:2}\x${mac:2:2}\x${mac:4:2}\x${mac:6:2}\x${mac:8:2}\x${mac:10:2}" | \
		dd of=$target conv=notrunc bs=1 seek=$mac_offset count=6
}

mtdname=`find_mtd_part "0:ART"`
mtdname=${mtdname//block/}
dd if=$mtdname of=/tmp/art.bin bs=64k count=1
mac1=$1 
mac2=$(macaddr_add $mac1 1)
echo "mac1 is: $mac1"
echo "mac2 is: $mac2"

#change_mac_withCRC $mac1 $mac_offset  $chksum_offset
# for ath11k mac_offset=4110,4116; chksum_offset=4106
change_mac_withCRC $mac1 4110 4106
change_mac_withCRC $mac2 4116 4106

mtd erase $mtdname
mtd write /tmp/art.bin $mtdname

#Usage: sh changemac.sh 88:12:4c:00:22:36