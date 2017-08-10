<?php

$link = mysqli_connect("mysql", "root", "", "mysql");

if(!$link){
	echo "Error: Unable to connect to MySQl." . PHP_EOL;
	echo "DEbugging errno: " . mysqli_connect_erron() . PHP_EOL;
	echo "Debugging error: " . mysqli_connect_error() . PHP_EOL;
	exit;
}

echo "Success: A proper connection to MySql was made! The mysql database is great." . PHP_EOL;
echo "Host information: " . mysqli_get_host_info($link) . PHP_EOL;

mysqli_close($link);

?>
