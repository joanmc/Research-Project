$sth = $dbh->prepare('SELECT name, colour, calories FROM fruit
    WHERE calories < :calories AND colour = :colour');
$sth->bindParam(':calories', $calories);
$sth->bindParam(':colour', $colour);
$sth->execute();
// $calories or $color do not need to be escaped or quoted since the
//    data is separated from the query