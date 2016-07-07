import pandas as pd
import MySQLdb as db
from datetime import datetime
import os

# CREATE A TABLE WITH AVERAGE NUM OF WIFI CONNECTIONS BETWEEN QUARTER PAST AND QUARTER TO THE HOUR IN A ROOM

# connect to database
con = db.connect(host="localhost", user="root", passwd='', db='MainDatabase')
cursor = con.cursor()

# create table
tname = 'AverageNumWifiConnections'
sql = "CREATE TABLE IF NOT EXISTS " + tname + " (DateTime datetime, Room VARCHAR(10), AvgNumWifiConn FLOAT, PRIMARY KEY (DateTime, Room))"
cursor.execute(sql)

# Dates and Times to be queried
Date = ['2015-11-03', '2015-11-04', '2015-11-05', '2015-11-06', '2015-11-09', '2015-11-10', '2015-11-11', '2015-11-12', '2015-11-13', '2015-11-16']
Time = ['09', '10', '11', '12', '13', '14', '15', '16', '17']

for d in Date:
    for t in Time:
        # set start date time and end datetime to query between
        start = "'" + d + " " + t + ":15:00'"
        end = "'" + d + " " + t + ":45:00'"
        # set datetime to enter into database (start of the hour being queried)
        datetime = d + " " + t + ":00:00"
        # Query B-004 between set datetime
        sql1 = "SELECT AVG(Associated) FROM Data.WiFiLogDataDT WHERE DateTime BETWEEN " + start + " AND " + end + " AND Room = 'B-004'"
        cursor.execute(sql1)
        res1 = cursor.fetchall()
        # insert result into table
        cursor.execute("INSERT INTO " + tname + " (DateTime, Room, AvgNumWifiConn) VALUES ('%s', '%s', %f)" % (datetime, 'B-004', res1[0][0]))
        con.commit() 
        # Query B-003 between set datetime 
        sql2 = "SELECT AVG(Associated) FROM Data.WiFiLogDataDT WHERE DateTime BETWEEN " + start + " AND " + end + " AND Room = 'B-003'"
        cursor.execute(sql2)
        res2 = cursor.fetchall()
        # insert result into table
        cursor.execute("INSERT INTO " + tname + " (DateTime, Room, AvgNumWifiConn) VALUES ('%s', '%s', %f)" % (datetime, 'B-003', res2[0][0]))
        con.commit() 
        # Query B-002 between set datetime
        sql3 = "SELECT AVG(Associated) FROM Data.WiFiLogDataDT WHERE DateTime BETWEEN " + start + " AND " + end + " AND Room = 'B-002'"
        cursor.execute(sql3)
        res3 = cursor.fetchall()
        # insert result into table
        cursor.execute("INSERT INTO " + tname + " (DateTime, Room, AvgNumWifiConn) VALUES ('%s', '%s', %f)" % (datetime, 'B-002', res3[0][0]))
        con.commit() 