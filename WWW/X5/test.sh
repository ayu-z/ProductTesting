#!/bin/sh

test() {
        sleep 10

        sn=`uci get 4g.server.sn`
        uci set test.server.sn=$sn

	. /lib/functions.sh
        config_load test
        uci commit test

        local start_num
        local hub_ok
        local hub_faile

        config_get hub_ok test hub_ok
        config_get hub_faile test hub_faile
        config_get start_num test start_num


        echo "-----read---->start_num:$start_num"
        echo "-----read---->hub_faile:$hub_faile"
        echo "-----read---->hub_ok:$hub_ok"

        let start_num+=1
        uci set test.test.start_num=$start_num

        Hub=`lsusb |grep "0bda:0411"|awk '{ print $6 }'`
        echo "--------->Hub_id:$Hub"

        if [ "0bda:0411"X == "$Hub"X ];then
                let hub_ok+=1
                uci set test.test.hub_ok=$hub_ok
        else
                let hub_faile+=1
                uci set test.test.hub_faile=$hub_faile
        fi

        echo "-----result---->start_num:$start_num"
        echo "-----result---->hub_faile:$hub_faile"
        echo "-----result---->hub_ok:$hub_ok"




        ##########################################
        local start_num_wifi
        local hub_ok_wifi
        local hub_faile_wifi

        config_get hub_ok_wifi test hub_ok_wifi
        config_get hub_faile_wifi test hub_faile_wifi
        config_get start_num_wifi test start_num_wifi


        echo "-----read---->start_num_wifi:$start_num_wifi"
        echo "-----read---->hub_faile_wifi:$hub_faile_wifi"
        echo "-----read---->hub_ok_wifi:$hub_ok_wifi"

        let start_num_wifi+=1
        uci set test.test.start_num_wifi=$start_num_wifi

       
        if [ -d /sys/class/net/wlan0 ];then
                let hub_ok_wifi+=1
                uci set test.test.hub_ok_wifi=$hub_ok_wifi
        else
                let hub_faile_wifi+=1
                uci set test.test.hub_faile_wifi=$hub_faile_wifi
        fi

        echo "-----result---->start_num_wifi:$start_num_wifi"
        echo "-----result---->hub_faile_wifi:$hub_faile_wifi"
        echo "-----result---->hub_ok_wifi:$hub_ok_wifi"
        ############################################



        uci commit test
}

