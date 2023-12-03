#!/bin/sh

authurl=$(uci get 4g.server.authurl)
fidpath=$(find /sys/ -name fid)
fid=$(cat $fidpath)
sn=$(uci get 4g.server.sn)
md5_str=$(echo -n ${sn}link4alliyunlinkadmin${fid} | md5sum | cut -d" " -f1)
auth_str=$(fw_printenv auth_str | cut -d"=" -f2 2>/dev/null)

i=0

try_auth() {
    while true; do
        if ping ${authurl%%/*} -c 2; then
            authcode=$(curl ${authurl}?r=auth/index\&mac=${sn}\&hid=${fid})
            if echo $authcode | grep -e "[0-9a-f]\{32\}"; then
                fw_setenv auth_str $authcode
                iptables -D INPUT -i br-lan -j DROP
                echo "get authed from internet!"
            fi
            break
        fi
        i=$(($i + 1))
        if [ $i -gt 20 ]; then
            break
        fi
        sleep 5
    done
}

if [ "$md5_str"x = "$auth_str"x ]; then
    echo "authed!"
    fw_setenv softauth 1
else
    fw_setenv softauth
    try_auth
    auth_str2=$(fw_printenv auth_str | cut -d"=" -f2 2>/dev/null)
    if [ "$md5_str"x != "$auth_str2"x ]; then
        echo "not authed,all packet will be drop in 500 second"
        sleep 500
        iptables -I INPUT -i br-lan -j DROP
    fi
fi
