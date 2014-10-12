<?php

require('../Site.conf');

// Set up connection
$link = mysqli_connect($SITEINFO['servername'],$SITEINFO['UserName'], $SITEINFO['password']) or die ('Unable to connect!');
mysqli_select_db($link,'FossilCalibration') or die ('Unable to select database!');

// get parameters

$calibration_id = mysqli_real_escape_string($link,$_GET['id']);

// set content-type header
header('Content-Type: application/json');

// Assemble query
$query = "SELECT * FROM View_Calibrations where CalibrationID = " . $calibration_id; 

$calibration_results = mysqli_query($link,$query) or die ('Error  in query: '.$query.'|'. mysqli_error());
if($calibration_results) {
	$row = mysqli_fetch_assoc($calibration_results);
	print json_encode($row);
	// convert to json
	mysqli_free_result($row);
}
mysqli_close($link);
?>
