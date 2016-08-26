


#!/bin/bash
#-#
#-#
#-# Author = Barry Kidney
#-#
#-#Script writes wifi signal strength to file at 5 min intervals

while :
do
#-# 	Enviroment Variables
	# Date Format --> YYYYMMDD-HHMM
	TIME=`date +%H:%M`
	DATE=`date +%d-%m-%Y`
	echo 'Tick '$TIME $DATE
	sleep 150
	echo 'WiFi signal stength at' $DATE $TIME >> /home/pi/WiFidB.txt
	iwconfig wlan0 | grep -i --color signal >> /home/pi/WiFidB.txt
	echo 'Tock '$TIME $DATE
	sleep 150

done