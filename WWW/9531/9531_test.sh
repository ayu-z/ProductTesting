#!/bin/bash


check=1000000
test_start(){

        echo 1=$1  2=$2  3=$3  4=$4
        sleep 20
        #固件版本检查，查看当下的固件是什么版本，与给定的版本对比，不一样才升级，第一个参数是固件路径加上固件名，第二个参数是要对比的固件版本，第三个参数是是否开启这个功能(1:开启 0：关闭)
#        check_upgrade_firmware 9531/2022-01-14-miniv2.bin 2022-01-14 1

        #固件升级功能，不管当下的固件是什么版本，都升级，第一个参数是固件路径加上固件名，第二个参数是是否开启功能(1:开启 0：关闭)
#        upgrade_firmware 9531/2022-01-04-miniv2.bin 0


        #模块检查 (1：检查 0：不检查）
#        check_module 1

        #SIM卡检查 (1：检查 0：不检查）
#        check_iccid 1

        #串口检查 (1：检查 0：不检查）
#       check_uart 1

        #设置MAC地址功能，当开启该功能时，不管之前有没有写过MAC,都会重新写MAC.(1:开启 0：关闭)
#        set_mac 0

        #检查MAC地址功能，当开启该功能时，之前没有写过MAC,会写MAC，若之前写过MAC,则不会再重新写MAC(1:开启 0：关闭)
#        check_mac_set 1

        #授权功能，当开启该功能时，不管之前是否有过授权,都会重新授权.(1:开启 0：关闭)
#        set_auth 1

        #检查功能，当开启该功能时，之前是没有过授权或授权码不对,就会授权，若之前受过权，就不会再授权.(1:开启 0：关闭)
#        check_auth_set 1

        #fw_setenv check $check
        #设置第一次启动，当重新设置过MAC，又没有进行固件升级时，需要开启这个功能
#        set_firstboot 1
}











upgrade_firmware(){
if [ "$2"x = "1"x ];then
	rm -rf /tmp/firmware.bin
	wget 192.168.11.100/$1 -O /tmp/firmware.bin
        echo  -e "--------\033[33m During the upgrade, make sure the power supply is normal. Please wait for 2-3 minutes \033[0m------------------"
        #sysupgrade -n firmware.bin > /tmp/null 2> /tmp/null
        mtd erase /dev/mtd6
        dd if=/tmp/firmware.bin of=/dev/mtd6
        firstboot -y
        sleep 1
        reboot
fi
}

check_upgrade_firmware(){
if [ "$3"x = "1"x ];then
	rm -rf /tmp/firmware.bin
	version=`cat /etc/openwrt_release|grep DISTRIB_BULDTIME|cut -d \' -f 2|cut -d ' ' -f 1`
	echo "------version:$version"
	echo "----------tmp:$2"
        check=`expr $check + 100000`

	if [ "$version"x != "$2"x ];then
		rm -rf firmware.bin
        	wget 192.168.11.100/$1 -O /tmp/firmware.bin
                echo  -e "--------\033[33m During the upgrade, make sure the power supply is normal. Please wait for 2-3 minutes \033[0m------------------"
		#sysupgrade -n firmware.bin > /tmp/null 2> /tmp/null
                
                mtd erase /dev/mtd6
                dd if=/tmp/firmware.bin of=/dev/mtd6
                firstboot -y
                reboot
	fi
fi
}




check_module(){
if [ "$1"x = "1"x ];then
	module=`ls /dev|grep ttyUSB2`
        	if [ "$module"x != "ttyUSB2"x ];then
                	sleep 3
                	module=`ls /dev|grep ttyUSB2`
                	if [ "$module"x != "ttyUSB2"x ];then
                	sleep 3
                        	module=`ls /dev|grep ttyUSB2`
                        	if [ "$module"x != "ttyUSB2"x ];then
                                	module="error"
                        	fi
                	fi
        fi

         at_tool AT*LWIPCTRL=mode,0,1
        sleep 1
        at_tool AT*LWIPCTRL=mode,0,1
        sleep 1
        at_tool AT*LWIPCTRL=mode,0,1
        sleep 1
        at_tool AT+YGFEATURECFG=512,1
         sleep 1
        at_tool AT+YGFEATURECFG=512,1
         sleep 1
        at_tool AT+YGFEATURECFG=512,1
         sleep 1
        at_tool AT+YGFEATURECFG=512,1
        sleep 1
        at_tool AT+PMODS=0
        sleep 1
        at_tool AT+PMODS=0
        sleep 1
        at_tool AT+PMODS=0


	if [ "$module"x = "error"x ];then
                 echo -e "---------\033[31m 1 \033[0m--------->module: \033[31m $module \033[0m"
        else
                 echo "--------- 1 --------->module:$module"
                 check=`expr $check + 10000`
                 echo "---------check:$check"
        fi
fi


}

check_iccid(){
if [ "$1"x = "1"x ];then
		iccid=`at_tool at+iccid|grep ICCID:|cut -d ":" -f2`
                if [ `echo $iccid|wc -c` -lt 20 ];then
                        sleep 3
                        iccid=`at_tool at+iccid|grep ICCID:|cut -d ":" -f2`
                        if [ `echo $iccid|wc -c` -lt 20 ];then
                                sleep 3
                                iccid=`at_tool at+iccid|grep ICCID:|cut -d ":" -f2`
                                if [ `echo $iccid|wc -c` -lt 20 ];then
                                        iccid="error"
                                fi
                        fi
                fi

		
		if [ "$iccid"x = "error"x ];then
                        echo -e "---------\033[31m 3 \033[0m--------->iccid: \033[31m $iccid \033[0m"
                else
                        echo "--------- 3 --------->iccid:$iccid"
                        check=`expr $check + 1000`
                        echo "---------check:$check"
                fi
fi
}



check_uart(){
if [ "$1"x = "1"x ];then
	/etc/init.d/seriald stop
	uci set 4g.modem.device=/dev/ttyS0
        uci commit 4g
        data="0123456789abcdefghijklmnopq11111111111111111111111111111"
        ttyS0=`at_tool $data|tr -d "\r\n" `
        if [ "$ttyS0"x != "$data"x ];then
              ttyS0="error"
        
        fi

        uci set 4g.modem.device=/dev/ttyUSB2
        uci commit 4g


	if [ "$ttyS0"x = "error"x ];then
                echo -e "---------\033[31m 2 \033[0m--------->ttyS0: \033[31m $ttyS0 \033[0m"
        else
                echo "---------2--------->ttyS0:$ttyS0"
                check=`expr $check + 100`
        fi
	/etc/init.d/seriald restart > /tmp/null 2> /tmp/null

fi
}



set_mac(){
if [ "$1"x = "1"x ];then
		wget 192.168.11.100 -O mac > /tmp/null 2> /tmp/null
                mac=`cat mac|tr -d :|tr "[A-Z]" "[a-z]"`

                /lib/setmac.sh ${mac:0:2} ${mac:2:2} ${mac:4:2} ${mac:6:2} ${mac:8:2} ${mac:10:2} > /dev/null 2>&1
                
                . /lib/functions.sh
                . /lib/functions/system.sh
                newmac=`mtd_get_mac_binary art 4098 |tr "[A-Z]" "[a-z]"|sed 's/://g'`

                #mac=`echo $mac|cut -d "\n" -f1`

                if [ "$mac" != "$newmac"  ];then 
                        newmac="error"
                fi


		if [ "$newmac"x = "error"x ];then
                        echo -e "---------\033[31m 4 \033[0m--------->newmac: \033[31m $newmac \033[0m"
                else
			echo  -e  "---------4--------->newmac:\033[33m $newmac \033[0m"
                fi

fi
}



check_mac_set(){
if [ "$1"x = "1"x ];then
		. /lib/functions.sh
                . /lib/functions/system.sh
                mac=`mtd_get_mac_binary art 4098 |tr "[A-Z]" "[a-z]"|sed 's/://g'`
		test="88124c"
         	result=$(echo $mac | grep "${test}")

		if [ "$result" == "" ];then
			wget 192.168.11.100 -O mac > /tmp/null 2> /tmp/null
	                mac=`cat mac|tr -d :|tr "[A-Z]" "[a-z]"`

	                /lib/setmac.sh ${mac:0:2} ${mac:2:2} ${mac:4:2} ${mac:6:2} ${mac:8:2} ${mac:10:2} > /dev/null 2>&1

        	        newmac=`mtd_get_mac_binary art 4098 |tr "[A-Z]" "[a-z]"|sed 's/://g'`
	
                	if [ "$mac" != "$newmac"  ];then
        	                mac="error"
	                fi

		fi
		
		if [ "$mac"x = "error"x ];then
                                echo -e "---------\033[31m 4 \033[0m--------->mac: \033[31m $mac \033[0m"
                else
			echo  -e  "---------4------------>mac:\033[33m $mac \033[0m"
                        check=`expr $check + 10`
                        echo "---------check:$check"
                fi

fi

}



set_auth(){
if [ "$1"x = "1"x ];then
		fidpath=`find /sys/ -name fid 2>/dev/null`
                hid=`cat $fidpath 2>/dev/null`
		. /lib/functions.sh
                . /lib/functions/system.sh
                mac=`mtd_get_mac_binary art 4098 |tr "[A-Z]" "[a-z]"|sed 's/://g'`


                authstr=`echo -en ${mac}link4alliyunlinkadmin${hid}|md5sum|awk '{print $1}'`
                fw_setenv auth_str $authstr
                fw_setenv softauth 1

                newauthstr=`echo -en|fw_printenv auth_str|cut -d "=" -f2`
                if [ "$authstr"x != "$newauthstr"x ];then
                        newauthstr="error"
                fi


                soft_auth=`echo -en|fw_printenv softauth|cut -d "=" -f2`
                if [ "$soft_auth"x != "1"x ];then
			soft_auth="error"
		fi

		if [ "$newauthstr"x = "error"x ];then
                        echo -e "---------\033[31m 5 \033[0m--------->newauthstr: \033[31m $newauthstr \033[0m"
                else
                        echo "--------- 5 --------->newauthstr:$newauthstr"
                fi

		if [ "$soft_auth"x = "error"x ];then
                        echo -e "---------\033[31m 5 \033[0m--------->soft_auth: \033[31m $soft_auth \033[0m"
                else
                        echo "--------- 5 --------->soft_auth:$soft_auth"
                fi
fi
}

check_auth_set(){
if [ "$1"x = "1"x ];then
		 fidpath=`find /sys/ -name fid 2>/dev/null`
                hid=`cat $fidpath 2>/dev/null`
                . /lib/functions.sh
                . /lib/functions/system.sh
                mac=`mtd_get_mac_binary art 4098 |tr "[A-Z]" "[a-z]"|sed 's/://g'`
                authstr=`echo -en ${mac}link4alliyunlinkadmin${hid}|md5sum|awk '{print $1}'`

                newauthstr=`echo -en|fw_printenv auth_str|cut -d "=" -f2`
                soft_auth=`echo -en|fw_printenv softauth|cut -d "=" -f2`

                if [ "$authstr"x != "$newauthstr"x -o "$soft_auth"x != "1"x ];then
			echo "--------- 5 --------->newauthstr:$newauthstr"
                        echo "--------- 5 --------->soft_auth:$soft_auth"
                        set_auth 1
		else
			echo "--------- 5 --------->newauthstr:$newauthstr"
                        echo "--------- 5 --------->soft_auth:$soft_auth"
                        check=`expr $check + 1`
                        echo "---------check:$check"
                fi
fi
}



set_firstboot(){
if [ "$1"x = "1"x ];then
        . /lib/functions.sh
        . /lib/functions/system.sh

        if_mac=`ifconfig br-lan|grep HWaddr|awk '{ print $5}'|sed 's/://g'|tr "[A-Z]" "[a-z]"`
        f_mac=`mtd_get_mac_binary art 4098 |tr "[A-Z]" "[a-z]"|sed 's/://g'`
        if [ "$if_mac"x != "$f_mac"x ];then
                echo "-----if_mac:$if_mac"
                echo "-----f_mac:$f_mac"
                echo  -e "--------\033[33m Set the first boot to restart the system \033[0m------------------"
                firstboot -y > /tmp/null 2> /tmp/null
                reboot
        fi
        
fi
}








