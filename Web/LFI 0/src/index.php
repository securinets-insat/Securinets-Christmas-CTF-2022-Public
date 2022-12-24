<html>
<head>
  <title>
LFI 0
  </title>
</head>
  <body background="bg.jpg">
    <h2>Source Code</h2>
    <?php show_source("source.php")?>
      -------------
  <h2>END of SRC code</h2>  
  -------------
<?php
   $var = $_GET['welcome'];
   if(isset($var))
   {
       include("$var");
   }

?>
