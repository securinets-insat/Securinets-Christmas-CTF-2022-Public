<?php
   $var = $_GET['welcome'];
   if(isset($var))
   {
       include("$var");
   }
   else
   {
       include("index.php");
   }
?>
