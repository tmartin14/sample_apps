<!DOCTYPE html>
<html>
<head>
  <title>CF PHP Hello World</title>
</head>
<body>
  <h1>Hello World!</h1>
<br/>This is a <b>PHP</b> app running on Cloud Foundry.<br/><br/><br/><b>Time:</b> 

<?php
    $t=time();
    echo(date("m/d/Y H:i:s",$t));
?>    
    
</body>
</html>
