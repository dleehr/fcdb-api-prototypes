<?php

require('../Site.conf');

// Set up connection
$link = mysqli_connect($SITEINFO['servername'],$SITEINFO['UserName'], $SITEINFO['password']) or die ('Unable to connect!');
mysqli_select_db($link,'FossilCalibration') or die ('Unable to select database!');

// get parameters
$filter = mysqli_real_escape_string($link,$_GET['filter']);

$min = mysqli_real_escape_string($link,$_GET['min']);
$max = mysqli_real_escape_string($link,$_GET['max']);

// set content-type header
header('Content-Type: application/json');

// Collect results
$calibrations = array();

// Assemble query
$query = "SELECT * FROM View_Calibrations where minAge > " . $min . " AND maxAge < " . $max;

$calibration_results = mysqli_query($link,$query) or die ('Error  in query: '.$query.'|'. mysqli_error());
while($row = mysqli_fetch_assoc($calibration_results)) {
	array_push($calibrations,$row);
	mysqli_free_result($row);
}
print json_encode($calibrations);
mysqli_close($link);
?>
