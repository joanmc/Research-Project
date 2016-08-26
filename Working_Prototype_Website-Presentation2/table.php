<?php include 'Sconfig.php'; ?>
<?php
	//Start session to hold global variables.
	session_start();

//	$room= "";
	$room = ($_GET['room']);
	$_SESSION["room"] = $room;
//	echo "ROOM + ".$room;

//				if(isset($_POST["submit"]))
//				{
//					$example = $_POST['example'];
//				}
//				echo $example;

	$conn->exec("set names utf8");
	$stmt1 = $conn->prepare("SELECT * FROM {$room}");
	$result1 = $stmt1->execute();
	$result1 = $stmt1->fetchAll(PDO::FETCH_ASSOC);


//echo "Room = ".$room;
//echo "Percent = ".$percent;
//echo "Binary = ".$binary;

//Timetable table
echo "<ul id=choice><li id='timetableToggle'><a href='#'>Timetable</a></li><li id='percentToggle'><a href='#'>Percentage</a></li><li id='binaryToggle'><a href='#'>Binary</a></li></ul></div>";

echo "<div id='timetableTable' clas='tables'><table>
	<tr>
		<th class='times'>Time</th>
		<th>Monday</th>
		<th>Tuesday</th>
		<th>Wednesday</th>
		<th>Thursday</th>
		<th>Friday</th>
	</tr>";

		foreach($result1 as $value)
			{
				echo "<tr>
				<td class='times'>".$value['Time']."</td>
				<td><a href='#'><div id=>".$value['Monday_Module']."</div></a></td>
				<td><a href='#'><div>".$value['Tuesday_Module']."</div></a></td>
				<td><a href='#'><div>".$value['Wednesday_Module']."</div></a></td>
				<td><a href='#'><div>".$value['Thursday_Module']."</div></a></td>
				<td><a href='#'><div>".$value['Friday_Module']."</div></a></td>
				</tr>
				<tr>
				<td><div></div></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				</tr>";
			}	
	echo "</table></div><br><br>";
//var_dump($result1);


//Percentage tables
	if($room == 'b002'){
		$percent = 'gt1p_b002';
	} elseif($room == 'b003'){
		$percent = 'gt1p_b003';
	} else{
		$percent = 'gt1p_b004';
	}

	$stmt2 = $conn->prepare("SELECT * FROM {$percent}");
	$result2 = $stmt2->execute();
	$result2 = $stmt2->fetchAll(PDO::FETCH_ASSOC);



echo "<div id='percentTable' class='tables'><table>
	<tr>
		<th class='times'>Time</th>
		<th>Monday</th>
		<th>Tuesday</th>
		<th>Wednesday</th>
		<th>Thursday</th>
		<th>Friday</th>
	</tr>";

	foreach($result2 as $value)
	{
		echo "<tr>
		<td class='times'>".$value['TIME']."</td>
		<td>".$value['MONDAY_WK1']."</td>
		<td>".$value['TUESDAY_WK1']."</td>
		<td>".$value['WED_WK1']."</td>
		<td>".$value['THURSDAY_WK1']."</td>
		<td>".$value['FRIDAY_WK1']."</td>
		</tr>";
	}
echo "</table></div><br><br>";
//	var_dump($result2);



//Binary Tables
	if($room == 'b002'){
		$binary = 'gt1b_b002';
	} elseif($room == 'b003'){
		$binary = 'gt1b_b003';
	} else{
		$binary = 'gt1b_b004';
	}

	$stmt3 = $conn->prepare("SELECT * FROM {$binary}");
	$result3 = $stmt3->execute();
	$result3 = $stmt3->fetchAll(PDO::FETCH_ASSOC);
//	var_dump($result3);


echo "<div id='binaryTable' class='tables'><table>
	<tr>
		<th class='times'>Time</th>
		<th>Monday</th>
		<th>Tuesday</th>
		<th>Wednesday</th>
		<th>Thursday</th>
		<th>Friday</th>
	</tr>";

	foreach($result3 as $value)
	{
		echo "<tr>
		<td class='times'>".$value['TIME']."</td>
		<td>".$value['MONDAY_WK1']."</td>
		<td>".$value['TUESDAY_WK1']."</td>
		<td>".$value['WED_WK1']."</td>
		<td>".$value['THURSDAY_WK1']."</td>
		<td>".$value['FRIDAY_WK1']."</td>
		</tr>";
	}
echo "</table></div>";
?>