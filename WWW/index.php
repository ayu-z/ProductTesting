<?php

$contents=file_get_contents("./mac.txt");
echo $contents;
$factoryid=substr($contents,0,6) ;
$macid=substr($contents,6,6) ;
$newmacid=dechex(hexdec($macid) +0x2);

file_put_contents("./mac.txt",$factoryid . $newmacid . "\n",LOCK_EX);
file_put_contents("./record.txt",$factoryid . $newmacid . "\t" . date("Y-m-d H:i:s") . "\n",FILE_APPEND | LOCK_EX);

