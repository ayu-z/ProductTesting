#!/bin/sh
pingip=`uci get system.@watchcat[0].pinghosts`
wanif=`uci get network.wan.ifname`
lteif=`uci get network.4g.ifname`



iswanon(){
  if ping $pingip -c1 -w1 -I $wanif 2>&1 > /dev/null;then
        echo  1
  else
        echo 0
  fi
}

ispppoeon(){
  if ping $pingip -c1 -w1 -I pppoe-wan 2>&1 > /dev/null;then
        echo  1
  else
        echo 0
  fi
}

islteon(){
  if ping $pingip -c1 -w1 -I $lteif 2>&1 > /dev/null;then
        echo  1
  else
        echo 0
  fi
}

while true
do
[ `uci get network.wan.ifname` = eth0.2 ] && {
      if ! swconfig dev switch0 show  |grep "port:3 link:up" > /dev/null 2>&1;then
      ifup wan
      sleep 2
      fi

[ "`uci get network.wan.proto`" = "dhcp" ] && [ "$(iswanon)" = "1" -a "`uci get network.wan.metric`" != "1" ] && {
uci set network.wan.metric=1
uci set network.4g.metric=3
uci  commit network
ifup wan
sleep 2
}

[ "`uci get network.wan.proto`" = "pppoe" ] && [  "$(ispppoeon)" = "1" -a "`uci get network.wan.metric`" != "1" ] && {
uci set network.wan.metric=1
uci set network.4g.metric=3
uci  commit network
ifup wan
sleep 2r
}

[ "$(ispppoeon)" = "1" -a "`uci get network.wan.metric`" != "1" ] && {
uci set network.wan.metric=1
uci set network.4g.metric=3
uci  commit network
ifup wan
sleep 2
}


[ "$(islteon)" = "1" -a "$(iswanon)" = "0" -a "$(ispppoeon)" = "0" ] && {
  [ "`uci get network.wan.metric`" != "4" ] && {
        uci set network.wan.metric=4
        uci commit network
        ifup wan
        }
}
}

sleep 1
done