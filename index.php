<!DOCTYPE html>
<!--most code is original but some has been sourced and adapted from www.w3schools.com-->

<!--import config file, connects to database-->
<?php
    require_once 'config.php';?>
<html>
    
    
    <head> 
        <meta charset="utf-8">
        <title>Home</title>
        <link rel="stylesheet" type="text/css" href="css/stylesheet.css">
    </head>
    
    
    
    <header><!--import header file, standard header on each page-->
        <?php 
            include 'header.php';?>
    </header>
    
    
    <body>
        
        <div class="centered" style="display: block; margin:0px auto 15px; padding: 5px 0px 5px 0px; height:100px;">           
            <form action="" method="POST" style="float: left" accept-charset="UTF-8">  
                
                
                Choose Campus:  
                <input type="radio" name="campus" value="Belfield" checked>Belfield 
                <input type="radio" name="campus" value="Blackrock">Blackrock<br><br>
        
                
                Enter Building:                  
                <select name="building" form="buildingForm" style="width: 100px" >
                    <option value="CS">Computer Science</option>
                </select>
                
                Enter Day:                  
                <select name="day" form="dayForm" style="width: 100px" >
                    <option value="2015-11-03">2015-11-03</option>
                    <option value="2015-11-04">2015-11-04</option>
                    <option value="2015-11-05">2015-11-05</option>
                </select>
                
                
                Enter Room:                  
                <select name="room" form="roomForm" style="width: 100px" >
                    <option value="B-002">B002</option>
                    <option value="B-003">B003</option>
                    <option value="B-004">B004</option>
                </select>
                
                <input type="submit" value="Submit">   
            </form>
        </div>
        
        
        
        <!--setting background image and overlay div-->
        <div style='background-image: url(images/UCDbackground.jpg); background-repeat: no-repeat; background-size: 100%'>
            <div class='centered' style='background-color: #f9f9f5; padding: 20px; opacity: 0.9; filter: alpha(opacity=90); max-width: 1000px; min-height: 550px; margin:0px auto 0px'>
        
            <?php
                
                if ($_SERVER['REQUEST_METHOD']=='POST'){
                
                if (isset($_POST['room'])) {
                    $requestedRoom = $_POST['room'];
                }
                echo $requestedRoom;
                
                $requestedCampus = 'Belfield';
//                echo "test".$_POST['room'];
                
//                $requestedRoom = 'B-004';
                $requestedDate = '2015-11-03 ';
                // beginning of table 
                echo "<table style='border=0; opacity: 1.0; filter: alpha(opacity=100);'><div><th width='25%'>Time</th><th width='25%'>Room&nbsp;Number</th><th width='25%'>Devices</th><th width='25%'>Estimated&nbsp;Occupants</th>";
                
                // connect to and query the database
                try {
                    $reply = $conn->query("SELECT Room, DateTime, Associated FROM wifilogdata WHERE DateTime LIKE '%{$requestedDate}%' AND Room = '{$requestedRoom}'"); 
                    $array = $reply->fetchAll(PDO::FETCH_ASSOC);
                    
                    // populate the table
                    foreach($array as $selected) {
                        $estimate = round($selected['Associated'] / 1.27);
                        echo "<tr><td width='25%'>".$selected['DateTime']."</td><td width='25%'>".$selected['Room']."</td><td width='25%'>".$selected['Associated']."</td><td width='25%'>".$estimate."</td></tr>";
                        }
                     }
                
                // error checking
                catch(PDOException $e) {
                     echo "Error".$e->getMessage();
                }
                $conn = null;
                }
                // close table
                echo"</table>"?>
            </div>
        </div>
    </body>
    
    
    <!--import footer file, standard footer on each page-->
    <footer>
        <?php 
            include 'footer.php';
        ?>
    </footer>  
    
</html>