<html>
<head>
  <title>
up to you
  </title>
</head>
  <body background="bg.jpg">
    <h2>Source Code</h2>
    <?php show_source("source.php")?>
      -------------
  <h2>END of SRC code</h2>  
  -------------
<?php
function greeting(){
  $a = file_get_contents(flag);
  echo 'all yours'.$a;
}
$a = [1, 2, 3];
$b = [10, 20, 30];
$custom_sum = $_GET['wassup'];
$int_array = array(0,1,2,3,4,5,6);
$new_array = array_map($custom_sum, $int_array);
$sum = array_map(function($x, $y) {
  return $x + $y;
}, $a, $b);

print_r($sum);

?>