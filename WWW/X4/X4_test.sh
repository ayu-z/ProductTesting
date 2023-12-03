#!/bin/bash

check=1000
test_start(){
        #模块检查 (1：检查 0：不检查）
        check_module 1
        #SIM卡检查 (1：检查 0：不检查）
        check_iccid 1

        #获取wifi名
        get_wifi_name 1

        #保存测试记录
        fw_setenv check $check

        #固件版本检查，查看当下的固件是什么版本，与给定的版本对比，不一样才升级，第一个参数是固件路径加上固件名，第二个参数是要对比的固件版本，第三个参数是是否开启这个功能(1:开启 0：关闭)
        check_upgrade_firmware X4/2021-12-06-m4pro-oldkernel.bin 2021-12-06 1

        #固件升级功能，不管当下的固件是什么版本，都升级，第一个参数是固件路径加上固件名，第二个参数是是否开启功能(1:开启 0：关闭)
        upgrade_firmware X4/2021-12-06-m4pro-oldkernel.bin 0
}


get_wifi_name(){
        if [ "$1"x = "1"x ];then
                wif2_4=`uci get wireless.@wifi-iface[0].ssid`
                echo  -e  "------------------>wif2_4:\033[33m $wif2_4 \033[0m"

                wif5_8=`uci get wireless.@wifi-iface[1].ssid`
                echo  -e  "------------------>wif5_8:\033[33m $wif5_8 \033[0m"
        fi

}



upgrade_firmware(){
if [ "$2"x = "1"x ];then
	rm -rf /tmp/firmware.bin
	wget 192.168.11.100/$1 -O /tmp/firmware.bin
        echo  -e "--------\033[33m During the upgrade, make sure the power supply is normal. Please wait for 2-3 minutes \033[0m------------------"
        #sysupgrade -n firmware.bin > /tmp/null 2> /tmp/null
      
        . /lib/upgrade/common.sh
        . /lib/functions.sh
        rootfs_mtd="/dev/mtd$(find_mtd_index rootfs)"
        fw_setenv have_fw 0
        run_ramfs "sync;mtd erase $rootfs_mtd;mtd write /tmp/firmware.bin $rootfs_mtd;sleep 2;reboot" 
fi
}

check_upgrade_firmware(){
if [ "$3"x = "1"x ];then
	rm -rf /tmp/firmware.bin
	version=`cat /etc/openwrt_release|grep DISTRIB_BULDTIME|cut -d \' -f 2|cut -d ' ' -f 1`
	echo  -e "------version:\033[33m $version \033[0m"
	echo "----------tmp: $2"
        check=`expr $check + 100`
        echo "---------check:$check"

	if [ "$version"x != "$2"x ];then
		rm -rf firmware.bin
		upgrade_firmware $1 1
                 
	fi
fi
}

check_module(){
if [ "$1"x = "1"x ];then
        for i in $(seq 1 4)
        do
                module=`uci -c /tmp/ get lte_info.card$i.imsi`
                if [ "$module"x == "NULL"x ];then
                        sleep 2
                        module=`uci -c /tmp/ get lte_info.card$i.imsi`
                        if [ "$module"x == "NULL"x ];then
                                module="error"
                        fi
                fi

                if [ "$module"x == "error"x ];then
                        echo -e "---------\033[31m 1 \033[0m----card$i----->module: \033[31m $module \033[0m"
                else
                        echo "-----1---- card$i --------->module:$module"
                        check=`expr $check + 10`
                        echo "-----card$i----check:$check"
                fi
        done
fi
}


check_iccid(){
if [ "$1"x = "1"x ];then
	for i in $(seq 1 4)
        do
               iccid=`uci -c /tmp/ get lte_info.card$i.iccid`
                if [ "$iccid"x == "NULL"x ];then
                        sleep 2
                         iccid=`uci -c /tmp/ get lte_info.card$i.iccid`
                         if [ "$iccid"x == "NULL"x ];then
                                iccid="error"
                        fi
                fi

                 if [ "$iccid"x == "error"x ];then
                        echo -e "---------\033[31m 2 \033[0m----card$i----->iccid: \033[31m $iccid \033[0m"
                else
                        echo "------2--- card$i --------->iccid:$iccid"
                        check=`expr $check + 1`
                        echo "-----card$i----check:$check"
                fi
        done
fi
}





set_firstboot(){
if [ "$1"x = "1"x ];then
        . /lib/functions.sh
        . /lib/functions/system.sh

        if_mac=`ifconfig br-lan|grep HWaddr|awk '{ print $5}'|sed 's/://g'|tr "[A-Z]" "[a-z]"`
        f_mac=`uci get 4g.server.sn`
        if [ "$if_mac"x != "$f_mac"x ];then
                echo "-----if_mac:$if_mac"
                echo "-----f_mac:$f_mac"
                echo  -e "--------\033[33m Set the first boot to restart the system \033[0m------------------"
                firstboot -y > /tmp/null 2> /tmp/null
                reboot
        fi
        
fi
}








