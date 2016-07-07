import pandas as pd
import xlrd
import MySQLdb as db
from dateutil.parser import parse
from datetime import datetime

# Read excel file containing ground truth data
df = pd.read_excel('CSI Occupancy Report.xlsx', sheetname='CSI')

# deparate individual table within data frame
# BETTER WAY TO DO THIS??? SEARCH FOR TABLES INSTEAD OF GIVING ACTUAL COLUMN AND ROW NUMBERS???
Mon1_Binary = df.iloc[6:20,:6].reset_index(drop=True)
# +20:+20
Mon1_Percentage = df.iloc[26:40,:6].reset_index(drop=True)
# +27:+27 
Tues1_Binary = df.iloc[53:67,:6].reset_index(drop=True)
# +20:+20
Tues1_Percentage = df.iloc[73:87,:6].reset_index(drop=True)
# +27:+27
Wed1_Binary = df.iloc[100:114,:6].reset_index(drop=True) 
# +20:+20
Wed1_Percentage = df.iloc[120:134,:6].reset_index(drop=True)  
# +28:+28
Thurs1_Percentage = df.iloc[148:162,:6].reset_index(drop=True)
# +20:+20
Thurs1_Binary = df.iloc[168:182,:6].reset_index(drop=True)
# +27:+27
Fri1_Binary = df.iloc[195:209,:6].reset_index(drop=True)
# +20:+20
Fri1_Percentage = df.iloc[215:229,:6].reset_index(drop=True)
# +26:+26
Mon2_Binary = df.iloc[241:255,:6].reset_index(drop=True)
# +20:+20
Mon2_Percentage = df.iloc[261:275,:6].reset_index(drop=True)
# +26:+26
Tues2_Binary = df.iloc[287:301,:6].reset_index(drop=True)
# +20:+20
Tues2_Percentage = df.iloc[307:321,:6].reset_index(drop=True)
# +26:+26
Wed2_Binary = df.iloc[333:347,:6].reset_index(drop=True)
# +20:+20
Wed2_Percentage = df.iloc[353:367,:6].reset_index(drop=True)
# +26:+26
Thurs2_Binary = df.iloc[379:393,:6].reset_index(drop=True)
# +20:+20
Thurs2_Percentage = df.iloc[399:413,:6].reset_index(drop=True)
# +26:+26
Fri2_Binary = df.iloc[425:439,:6].reset_index(drop=True)
# 20:+20
Fri2_Percentage = df.iloc[445:459,:6].reset_index(drop=True)

# List of all dataframes containing tables with ground truth data
df_list = [Mon1_Binary, Mon1_Percentage, Tues1_Binary, Tues1_Percentage, Wed1_Binary, Wed1_Percentage, Thurs1_Percentage,
      Thurs1_Binary, Fri1_Binary, Fri1_Percentage, Mon2_Binary, Mon2_Percentage, Tues2_Binary, Tues2_Percentage, 
      Wed2_Binary, Wed2_Percentage, Thurs2_Binary, Thurs2_Percentage, Fri2_Binary, Fri2_Percentage]

class groundTruth():
    def __init__(self, name):
        # Connect to database
        self.con = db.connect(host="localhost", user="root", passwd='', db=name)
        self.cursor = self.con.cursor()
        
    def createTable(self, tname):
        # Create ground truth table - same for binary table and percentage table
        sql = "CREATE TABLE IF NOT EXISTS " + tname + " (DateTime datetime, Room VARCHAR(10), GroundTruth FLOAT, PRIMARY KEY (DateTime, Room))"
        self.cursor.execute(sql)
        return
    
    # Add file is the same for Binary and Percentage tables EXCEPT the date is contained in a different row
    def addFileB(self, tname, df, room, index): 
        # Each table contains data for all rooms for one day so date stays the same for each datarame that is added
        date = parse(df.iloc[1][0]).strftime('%Y-%m-%d')
        for i in range(6, len(df)):
            # split the time cell (9:00-10:00), only the time the class starts at goes into the database (09:00)
            t = df.iloc[i][0].split('-')
            self.cursor.execute("INSERT INTO " + tname + " (Datetime, Room, GroundTruth) VALUES('%s', '%s', %f)"  % (pd.to_datetime(date + ' ' + datetime.strptime(t[0], "%H.%M").strftime('%H:%M:%S')), room, df.iloc[i][index]))
            self.con.commit()           
        return
    
    def addFileP(self, tname, df, room, index): 
        date = parse(df.iloc[2][0]).strftime('%Y-%m-%d')
        for i in range(6, len(df)):
            t = df.iloc[i][0].split('-')
            self.cursor.execute("INSERT INTO " + tname + " (Datetime, Room, GroundTruth) VALUES('%s', '%s', %f)"  % (pd.to_datetime(date + ' ' + datetime.strptime(t[0], "%H.%M").strftime('%H:%M:%S')), room, df.iloc[i][index]))
            self.con.commit()           
        return

# Connect to database
name = 'MainDatabase'
myData = groundTruth(name)

# Table for binary ground truth info
tnameB = 'GroundTruth_Binary'
myData.createTable(tnameB)

# Table for percentage ground truth info
tnameP = 'GroundTruth_Percentage'
myData.createTable(tnameP)

# Room: B004 Column: 2
# Room: B003 Column: 5
# Room: B002 Column: 4

# add binary ground truth info for B004
room = 'B-004'
for i in range(0,len(df_list),2):
    myData.addFileB(tnameB, df_list[i], room, 2)

# add percentage ground truth info for B004
room = 'B-004'
for i in range(1,len(df_list),2):
    myData.addFileP(tnameP, df_list[i], room, 2)
    
# add binary ground truth info for B003    
room = 'B-003'
for i in range(0,len(df_list),2):
    myData.addFileB(tnameB, df_list[i], room, 5)

# add percentage ground truth info for B003
room = 'B-003'
for i in range(1,len(df_list),2):
    myData.addFileP(tnameP, df_list[i], room, 5)

# add binary ground truth info for B002
room = 'B-002'
for i in range(0,len(df_list),2):
    myData.addFileB(tnameB, df_list[i], room, 4)

# add percentage ground truth info for B002
room = 'B-002'
for i in range(1,len(df_list),2):
    myData.addFileP(tnameP, df_list[i], room, 4)