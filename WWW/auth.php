<?php
// echo phpinfo();
header('Content-type: text/plain');

echo md5($_GET['mac'] . "link4alliyunlinkadmin" . $_GET['hid']);

