<!DOCTYPE html>

<html>
	<head>
		<title>Scratch</title>
		
		<meta charset="utf-8">
		<link rel="stylesheet" type="text/css" href="#">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
		<link href='https://fonts.googleapis.com/css?family=Chicle' rel='stylesheet' type='text/css'>
		<link rel="stylesheet" type="text/css" href="css/style.css">
	</head>
	
	<body>
		<div id="container">
		<header>
			<h2>Ocu-Pants</h2>
		</header>
		
		<?php include 'Sconfig.php'; ?>
		
		<div>
			<form id="roomForm">

                <select name="example" onchange="showRoom(this.value)" id="roomSelect">
                    <option value="">Select Room</option>
                    <option value="b002">B-002</option>
                    <option value="b003">B-003</option>
                    <option value="b004_wk1">B-004(wk1)</option>
					<option value="b004_wk2">B-004(wk2)</option>
                </select>
                
                <br><br>
                
<!--                <input name="submit" type="submit" />-->
            </form>   
		</div>
		
		<div id="tables"></div>
		<div id="extra"></div>
<!--		Function using AJAX to change the tables in the page
-->
	<script>
		function showRoom(room)
		{
			if (room == "") 
			{
				document.getElementById("table").innerHTML = "";
				return;
			} 
			else
			{
				var xmlhttp = new XMLHttpRequest();
				xmlhttp.onreadystatechange = function() 
				{
					if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
					{
						document.getElementById("tables").innerHTML = xmlhttp.responseText;
					}
				};
				console.log("ajaxtest.php?q="+room);
				xmlhttp.open("POST","table.php?room="+room,true);
				xmlhttp.send();	
			}
		};
</script>
<script>
		$(document).ready(function(){
			$('#tables').on('click','#timetableToggle', function(){
				$('#timetableTable').toggle("fast");
			});	
			$('#tables').on('click','#percentToggle', function(){
				$('#percentTable').toggle("fast");
			});	
			$('#tables').on('click','#binaryToggle', function(){
				var ids = ['#percentToggle','#binaryToggle','off'];
				$('#binaryTable').toggle("fast");
			});	
			
			$('#choice').on('click', '#toggle', function(){
				  $('div').each(function(){
					var classes = ['class1','class2','class3'];
					this.className = classes[($.inArray(this.className, classes)+1)%classes.length];
				  });
				});
			
			
			$('#tables').on('click','td', function(){
				//Extracting the module info
				var module = $(this).text();
				console.log(module);
				
				//Extracting the time info
				//Source: http://stackoverflow.com/questions/25198699/javascript-get-data-of-first-cell-of-selected-table-row
				var time = $(this).parent().find('.times').text();
				console.log("time="+time);
				time = time.trim().substring(0, 5); 
				console.log("time="+time);
				
				
				var xmlhttp = new XMLHttpRequest();
				xmlhttp.onreadystatechange = function() 
				{
					if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
					{
						document.getElementById("extra").innerHTML = xmlhttp.responseText;
					}
				};
				console.log("ajaxtest.php?module="+module);
				xmlhttp.open("POST","extra.php?module="+module+"&time="+time,true);
				xmlhttp.send();
				
			});
			
//			$("#tables").on('click', '.tables',function() {
//				$('html, body').animate({
//					scrollTop: $("#choice").offset().top
//				}, 2000);
//			});
			
//			$('#tables').on('mouseenter','td', function(){
//				$(this).css('color', 'red');
//			});
		});
</script>

	</div>
	</body>


</html>