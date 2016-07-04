<!--some of the code was sourced and adapted from w3schools and stackoverflow-->
<!--this file contains the information for connecting to the database-->


<?php
//    echo "Apache Works!";
    $host = 'localhost';
    $dbname = 'data1';
    $username = 'root';
    $password = '';

try {
    // connect to database
    $conn = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // set return characters to utf8
    $conn->exec("set names utf8");
//    echo "Connected to $dbname at $host successfully.";
} 
catch (PDOException $pe) {
    // error handling
    die("Connection to the database: $dbname failed" . $pe->getMessage());
}
?>


    