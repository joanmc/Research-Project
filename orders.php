<!DOCTYPE html>
<!--most code is original but some has been sourced and adapted from www.w3schools.com-->

<!--import config file, connects to database-->
<?php
    require_once 'config.php';?>
<html>  
    
    
    <head>
        <meta charset="utf-8">
        <title>Orders</title>
        <link rel="stylesheet" type="text/css" href="css/stylesheet.css">
    </head>
    
    
    
    <header><!--import header file, standard header on each page-->
        <?php 
            include 'header.php';?>
    </header>
    
    
    <body>
        <!--setting background image and overlay div-->
        <div style='background-image: url(images/background2.jpg); background-repeat: repeat-y; background-size: 100%'>
            <div class='centered' style='background-color: #f9f9f5; padding: 20px; opacity: 0.8; filter: alpha(opacity=80); max-width: 1000px; min-height: 550px; margin:0px auto 0px'>
            <h1>Orders</h1>

            <?php
                // 3 connections required one for each query
                $conn = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);// first connection
                // first the query for the in progress orders
                $reply = $conn->query("SELECT * FROM orders INNER JOIN orderdetails ON orders.orderNumber=orderdetails.orderNumber INNER JOIN products ON orderdetails.productCode=products.productCODE WHERE orders.status ='In process' GROUP BY orders.orderNumber DESC");
                $array = $reply->fetchAll(PDO::FETCH_ASSOC);// cast reply ro an array

  
                $conn1 = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);// second conection
                // second the query for the cancelled orders
                $reply1 = $conn1->query("SELECT * FROM orders INNER JOIN orderdetails ON orders.orderNumber=orderdetails.orderNumber INNER JOIN products ON orderdetails.productCode=products.productCODE WHERE orders.status ='Cancelled' GROUP BY orders.orderNumber DESC");
                $array1 = $reply1->fetchAll(PDO::FETCH_ASSOC);// cast reply ro an array
                
                
                $conn2 = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);// third connection
                // third the query for the 20 most recent orders
                $reply2 = $conn2->query("SELECT * FROM orders INNER JOIN orderdetails ON orders.orderNumber=orderdetails.orderNumber INNER JOIN products ON orderdetails.productCode=products.productCODE GROUP BY orders.orderNumber DESC LIMIT 20");
                $array2 = $reply2->fetchAll(PDO::FETCH_ASSOC);// cast reply ro an array
                ?>
             
                
            
<!--            create the order in process table-->
            <div class="centered">
                <h1>In process (click on the order number to see more information)</h1>

                <?php
                    // make first row of table
                    echo "<table><tr><th>Number</th><th>Date</th><th>Status</th></tr>";
                    // populate the table
                    
                    foreach($array as $selected) {
                        $number = $selected['orderNumber'];
                        echo "<tr onclick='orderInfo($number)'><td>".$selected['orderNumber']."</td><td>".$selected['orderDate']."</td><td>".$selected['status']."</td></tr>";
                    }
                    // close the table
                    echo"</table>"?> 
            </div>
   
<!--            create the specific order table-->
            <div class="centered">
                <?php   
                        // create the specific order table and set its unique id number
                        foreach($array as $selected) {
                            $number = $selected['orderNumber'];
                            
                            echo "<table id='$number' style = 'display: none; border: 1px solid black'><tr><th>Order Number</th><th>Product Name</th><th>Product Line</th><th>Product Code</th><th>Order Date</th><th>Required Date</th><th>Shipped Date</th><th>Status</th><th>Comments</th><th>Customer Number</th></tr>";
                            echo "<tr><td>".$selected['orderNumber']."</td><td>".$selected['productName']."</td><td>".$selected['productLine']."</td><td>".$selected['productCode']."</td><td>".$selected['orderDate']."</td><td>".$selected['requiredDate']."</td><td>".$selected['shippedDate']."</td><td>".$selected['status']."</td><td>".$selected['comments']."</td><td>".$selected['customerNumber']."</td></tr>";       
                    }
                // close the table
                echo "</table>";?>
            </div>
    
                
                
                
                
<!--            the cancelled order table same process as the in process table see above for comments-->             
            <div class="centered">
                <h1>Cancelled orders (click on the order number to see more information)</h1>

                <?php
                    echo "<table><tr><th>Number</th><th>Date</th><th>Status</th></tr>";
                    foreach($array1 as $selected) {
                        $number = $selected['orderNumber'];
                        echo "<tr onclick='orderInfo($number)'><td>".$selected['orderNumber']."</td><td>".$selected['orderDate']."</td><td>".$selected['status']."</td></tr>";
                    }
                echo"</table>"?>
            </div>
    
                
            <div class="centered">
               <?php
                    foreach($array1 as $selected) {
                        $number = $selected['orderNumber'];

                        echo "<table id='$number' style = 'display: none; border: 1px solid black'><tr><th>Order Number</th><th>Product Name</th><th>Product Line</th><th>Product Code</th><th>Order Date</th><th>Required Date</th><th>Shipped Date</th><th>Status</th><th>Comments</th><th>Customer Number</th></tr>";
                        echo "<tr><td>".$selected['orderNumber']."</td><td>".$selected['productName']."</td><td>".$selected['productLine']."</td><td>".$selected['productCode']."</td> <td>".$selected['orderDate']."</td><td>".$selected['requiredDate']."</td><td>".$selected['shippedDate']."</td><td>".$selected['status']."</td><td>".$selected['comments']."</td><td>".$selected['customerNumber']."</td></tr></table>";}?>
            </div>
            
                
                
                
                
                
                
                
                
<!--            the last 20 orders table same process as the in process table see above for comments-->
            <div class="centered">
                <h1>20 most recent orders (click on the order number to see more information)</h1>

                <?php
                    echo "<table><tr><th>Number</th><th>Date</th><th>Status</th></tr>";
                    foreach($array2 as $selected) {
                        $number = $selected['orderNumber'];
                        echo "<tr onclick='orderInfo($number)'><td>".$selected['orderNumber']."</td><td>".$selected['orderDate']."</td><td>".$selected['status']."</td></tr>";
                    }
                echo "</table>"?> 
            </div>
    
  
            <div class="centered">
               <?php
                    foreach($array2 as $selected) {
                        $number = $selected['orderNumber'];

                        echo "<table id='$number' style = 'display: none; border: 1px solid black'><tr style = 'border: 1px solid black;'><th>Order Number</th><th>Product Name</th><th>Product Line</th><th>Product Code</th><th>Order Date</th><th>Required Date</th><th>Shipped Date</th><th>Status</th><th>Comments</th><th>Customer Number</th></tr>";
                        echo "<tr><td>".$selected['orderNumber']."</td><td>".$selected['productName']."</td><td>".$selected['productLine']."</td> <td>".$selected['productCode']."</td><td>".$selected['orderDate']."</td><td>".$selected['requiredDate']."</td><td>".$selected['shippedDate']."</td><td>".$selected['status']."</td><td>".$selected['comments']."</td><td>".$selected['customerNumber']."</td></tr></table>";  
                    };?>
                </div>
            </div>
        </div>               
    </body>
    
    <footer>
        <?php 
            include 'footer.php';
        ?>
    </footer>
    
    <!--function to control the visability of divs (would have avoided the page refreshing), this approach was not implemented due to time constraints-->
    <script>    
        function orderInfo(x) {
            
            <?php
                foreach($array as $selected) {
                    $number = $selected['orderNumber'];
                    echo "document.getElementById($number).style.display = 'none';";
                }
                foreach($array1 as $selected) {
                    $number = $selected['orderNumber'];
                    echo "document.getElementById($number).style.display = 'none';";
                }
                foreach($array2 as $selected) {
                    $number = $selected['orderNumber'];
                    echo "document.getElementById($number).style.display = 'none';";
                }?>
            
            document.getElementById(x).style.display = 'block';
        }
    </script>
</html>