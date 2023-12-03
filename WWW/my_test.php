<?php
$Aid = $_REQUEST['Aid'];
$Acd = $_REQUEST['Acd'];
$data = array();
$data[] = array('Aid_response'=> $Aid, 'Acd_response'=> $Acd);
echo json_encode($data);
?>