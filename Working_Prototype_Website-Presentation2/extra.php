<?php include 'Sconfig1.php'; ?>

<?php
session_start();
$module = ($_GET['module']);
$_SESSION["module"] = $module;
$time = ($_GET['time']);
$_SESSION["time"] = $time;
$room = $_SESSION["room"];
//echo $Date.$time;
//
//print_r($_SESSION);
//echo "<br>Room: ".$room;
//echo "<br>Time is ".$time;
if($room == "b002"){
	$room = "B-002";
}elseif($room == "b003"){
	$room = "B-003";
}else{
	$room = "B-004";
}

//echo "<br>Room: ".$room;


	$conn->exec("set names utf8");
//	$stmt1 = $conn->prepare("SELECT AvgNumWifiConn, GroundTruth FROM final WHERE Room = '{$room}' AND DateTime LIKE '%{$time}'");
	$stmt1 = $conn->prepare("SELECT * FROM final WHERE Module = '{$module}' AND Room = '{$room}'");
	$stmt2 = $conn->prepare("SELECT * FROM modules WHERE ModuleTitle = '{$module}'");
	$stmt3 = $conn->prepare("Select * FROM Rooms");
		
		
	$result1 = $stmt1->execute();
	$result2 = $stmt2->execute();
	$result3 = $stmt3->execute();

	$result1 = $stmt1->fetchAll(PDO::FETCH_ASSOC);
	$result2 = $stmt2->fetchAll(PDO::FETCH_ASSOC);
	$result3 = $stmt3->fetchAll(PDO::FETCH_ASSOC);

echo "<div><table>
					<tr>
						<th>Class Time</th>
						<th>Room Capacity</th>
						<th>Students Registered</th>
						<th>Avg Wifi Connections</th>
						<th>Estimated Occupancy</th>
						<th>GroundTruth Occupancy</th>
					</tr>
					";

foreach($result1 as $value1){
	foreach($result2 as $value2){
		$estimate = $value1['AvgNumWifiConn']/1.27;
		$percent = round((float)$value1['GroundTruth']*100 ).'%';
		$wifi = $value1['AvgNumWifiConn'];
//		echo $wifi;
		
		echo "<tr>
				<td>".$value1['DateTime']."</td>
				<td>?</td>
				<td>".$value2['NumberRegistered']."</td>
				<td>".round($wifi)."</td>
				<td>".round($estimate)."</td>
				<td>".$percent."</td>
			</tr>";

	}
}
echo "</table></div>";


//
//	var_dump($result1);
//	var_dump($result2);
//	var_dump($result3);



//
//
//
//                        
//                        
//                        
//                        
//                        $reply = $conn->prepare("SELECT AVG(Associated) FROM wifilogdata WHERE Date = '{$requestedDate}' AND Room = '{$example}' AND Time > '{$time2}' AND  Time < '{$time3}'");
//                        $reply->execute();


?>