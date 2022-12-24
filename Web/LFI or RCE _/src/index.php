<?php session_start(); ?>
<html>
<head>
  <title>
LFI or RCE?
  </title>
</head>
  <body background="bg.jpg">
    <h2>Source Code</h2>
    <?php show_source("source.php")?>
      -------------
  <h2>END of SRC code</h2>  
  -------------
<?php
if(isset($_GET["fathi"])){
  $t = $_GET["fathi"];
  if (preg_match('/\.\.\//', $t)) {
    die('haacker!! ejrili ya fathi');
  }
$_SESSION["fathi"]=$t;
include("/tmp".$t);
}
?>
