<?php
$url = $_GET['url'];
if (isset($url) && strlen($url) < 17){
$ch = curl_init($url);
curl_setopt($ch, CURLOPT_REDIR_PROTOCOLS, CURLPROTO_HTTP);
curl_setopt($ch, CURLOPT_PROTOCOLS, CURLPROTO_HTTP);
curl_setopt($ch, CURLOPT_MAXREDIRS, 1);

echo curl_exec($ch);
curl_close($ch);
}
else{
echo 'welcome, set get param with maximum 16 chars.. I got some secret in my internals.. called flag.txt';
}
?>