<!DOCTYPE html>
    <!--most code is original but some has been sourced and adapted from www.w3schools.com-->

    <?php
        require_once 'config.php';?><!--import config file, connects to database-->

<html>
    <head> 
        <meta charset="utf-8">
<!--        <link rel="stylesheet" type="text/css" href="css/stylesheet.css">-->
        <link rel="icon" href="/t4cms/ucdmaincore_favicon.ico">
        <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700,800|Roboto+Slab:100,200,300,400" rel="stylesheet" type="text/css">
        <title>University College Dublin</title>
    </head>
    
    <header><!--import header file, standard header on each page-->
        <?php 
            include 'header.php';?>
    </header>
    
    <body>
        <div class="centered" style="display: block; margin:0px auto 15px; padding: 5px 0px 5px 0px; height:100px;">  
            <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="post">

                <select name="example">
                    <option selected="selected" value="B-002">B-002</option>
                    <option value="B-003">B-003</option>
                    <option value="B-004">B-004</option>
                </select>
                
                <br>
                
                <select name="example3">
                    <option selected="selected" value="2015-11-03">2015-11-03</option>
                    <option value="2015-11-04">2015-11-04</option>
                    <option value="2015-11-05">2015-11-05</option>
                    <option value="2015-11-06">2015-11-06</option>
                    <option value="2015-11-07">2015-11-07</option>
                    <option value="2015-11-08">2015-11-08</option>
                    <option value="2015-11-09">2015-11-09</option>
                    <option value="2015-11-10">2015-11-10</option>
                    <option value="2015-11-11">2015-11-11</option>
                    <option value="2015-11-12">2015-11-12</option>
                    <option value="2015-11-13">2015-11-13</option>
                    <option value="2015-11-14">2015-11-14</option>
                    <option value="2015-11-15">2015-11-15</option>
                    <option value="2015-11-16">2015-11-16</option>
                    <option value="2015-11-17">2015-11-17</option>
                </select>
                
                <input name="submit" type="submit" />
            </form>   
        </div>
            
                <!--setting background image and overlay div-->
        <div style='background-image: url(images/UCDbackground.jpg); background-repeat: no-repeat; background-size: 100%'>
            <div class='centered' style='background-color: #f9f9f5; padding: 20px; opacity: 0.9; filter: alpha(opacity=90); max-width: 1000px; min-height: 550px; margin:0px auto 0px'>
        
        
            <?php
                
                function AvgDevices($arr, $time, $date) {
                    $avgDevs = 0;
                    $counter = 0;

                    foreach($arr as $selected) {
                        if ($selected['Date'] == $date and strtotime($selected['Time']) >= $time+(60*15) and strtotime($selected['Time']) <= $time+(60*45)) {
                            $avgDevs = $avgDevs + $selected['Associated'];
                            $counter = $counter + 1; 
                        }
                    } if ($counter > 0) {
                        return $avgDevs/$counter;
                    } else {
                        return 0;
                    }
                }
                
                
                
                if (isset($_POST['submit']) && !empty($_POST['submit'])) {
                    
                    $example = $_POST['example'];
                    $requestedDate = $_POST['example3'];
                    $requestedCampus = 'Belfield';
                    $requestedBuilding = 'Computer Science';
                    
                    echo $example . "<br>";
                    echo $requestedDate . "<br>";
                    echo $requestedCampus . "<br>";
                    echo $requestedBuilding . "<br>";


                    

                    try { 
                        // construct query
                        $reply = $conn->prepare("SELECT Associated, Date, Time FROM wifilogdata WHERE Room = '{$example}' AND Time >= '09:00:00' AND Time <= '18:00:00'");                        
                        
                        // query the database
                        $reply->execute();
                
                        //error case
                        if(!$reply) {
                            die("Execute query error");
//                          die("Execute query error, because: ". $conn->errorInfo());
                        
                        } else {
                            $array = $reply->fetchAll(PDO::FETCH_ASSOC);

                            // beginning of table 
                            echo "<table style='opacity: 1.0; filter: alpha(opacity=100);'><div><th width='25%'>Time</th><th width='25%'>Devices</th><th width='25%'>Estimated&nbsp;Occupants</th>";
                            
                            // populate the table
                            for($z=strtotime('09:00:00'); $z<strtotime('09:00:00')+(60*60*9); $z+=(60*60)) {
                                $devices = AvgDevices($array, $z, $requestedDate);                
                                $estimate = round($devices/1.27);
                                echo "<tr><td width='25%'>".date("H:i:s", $z)."</td><td width='25%'>".$devices."</td><td width='25%'>".$estimate."</td></tr>";
                            }
                        }
                    } catch(PDOException $e) {
                        echo "Error".$e->getMessage();
                    }
                
                $conn = null;
                // close table
                echo"</table>";
                
                } else {
                    echo "submit not registered.";
                }?>
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