<?php
session_start();
highlight_file(__FILE__);
if(isset($_GET["fathi"])){
  $t = $_GET["fathi"];
  if (preg_match('/\.\.\//', $t)) {
    die('haacker!! ejrili ya fathi');
  }
$_SESSION["fathi"]=$t;
include("/tmp".$t);
}
?>