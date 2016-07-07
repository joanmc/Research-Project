import pandas as pd
import xlrd
import MySQLdb as db
from dateutil.parser import parse
from datetime import datetime
from datetime import timedelta

# This is just to find where each thing was.. date, time, module etc...
# DATE - EVERY SECOND COLUMN ROW 0
# i CONTROLS COLUMN NUMBER
print(df.iloc[0][3] + ' November 2015')
d = parse(df.iloc[0][3] + ' November 2015').strftime('%Y-%m-%d')
print(d, type(d))

# TIME - COLUMN 0 FROM ROW 1
# j CONTROLS ROW NUMBER
t = df.iloc[2][0].split(' - ')
time = datetime.strptime(t[0], "%H:%M").strftime('%H:%M:%S')
print(datetime.strptime(t[0], "%H:%M").strftime('%H:%M:%S'))
print(type(pd.to_datetime(d + ' ' + time)))

# Module - Every 2nd column from column 1 from row 1 to end
# df.iloc[row][column]
df.iloc[1][3]

class timetable():
    def __init__(self, name):
        # connect to the database
        self.con = db.connect(host="localhost", user="root", passwd='', db=name)
        self.cursor = self.con.cursor()
        
    def createTableTimeModule(self, tname):
        # create table with modules and the time
        sql = "CREATE TABLE IF NOT EXISTS " + tname + " (DateTime datetime, Room VARCHAR(10), Module VARCHAR(30) NOT NULL, PRIMARY KEY (DateTime, Room))"
        self.cursor.execute(sql)
        
    def createTableModule(self, tname):
        # Create Modules table
        sql = "CREATE TABLE IF NOT EXISTS " + tname + " (ModuleName VARCHAR(30), NumReg INT, PRIMARY KEY(ModuleName))"
        self.cursor.execute(sql)
        
    def createTableTimetable(self, tname):
        # Create Timetable table
        sql = "CREATE TABLE IF NOT EXISTS " + tname + " (Time VARCHAR(20), Monday_Module VARCHAR(80), Monday_NumReg INT, Tuesday_Module VARCHAR(40),Tuesday_NumReg INT, Wednesday_Module VARCHAR(40), Wednesday_NumReg INT, Thursday_Module VARCHAR(40), Thursday_NumReg INT, Friday_Module VARCHAR(40), Friday_NumReg INT)"
        self.cursor.execute(sql)
        
    def fixLecPrac(self, df):
        # List to keep track of modules that have practicals
        module_list = []
        for i in range(1,10,2): # go through columns
            for j in range(1,len(df)-1): # go through rows
                if df.iloc[j][i]:  # If there is a module on check if it is a double (i.e. a practical)
                    if df.iloc[j][i] == df.iloc[j+1][i]: # if module is the same as the module in the next hour mark it as a practical
                        # Practicals can occur more than once, each with different numbers of students registered
                        # Keep track of practicals and if first practical ('P1') for module has already occured mark as second practical ('P2')
                        if df.iloc[j][i] in module_list: 
                            module_list.append(df.iloc[j][i])
                            df.iloc[j][i] = df.iloc[j][i] + "P2"
                            df.iloc[j+1][i] = df.iloc[j+1][i] + "P2"
                        else:
                            module_list.append(df.iloc[j][i])
                            df.iloc[j][i] = df.iloc[j][i] + "P1"
                            df.iloc[j+1][i] = df.iloc[j+1][i] + "P1"
        return df
        
    def addTimeModuleWk1(self, tname, df, room):
        # add data
        for i in range(1, 10, 2): # column DATE
            date = parse(df.iloc[0][i] + ' November 2015').strftime('%Y-%m-%d')
            for j in range(1, len(df)): # row TIME
                t = df.iloc[j][0].split(' - ')
                self.cursor.execute("INSERT INTO " + tname + "(DateTime, Room, Module) VALUES('%s', '%s', '%s')" % (pd.to_datetime(date + ' ' + datetime.strptime(t[0], "%H:%M").strftime('%H:%M:%S')), room, df.iloc[j][i]))
                self.con.commit()           
        return
    
    def addTimeModuleWk2(self, tname, df, room):
        # Same as addTimeModuleWk1 but the date has to be incremented by seven days
        # Has to be done like this because the timetables in the csv files have the dates for week 1 on the week 2 timetable
        for i in range(1, 10, 2): # column DATE
            date = (parse(df.iloc[0][i] + ' November 2015') + timedelta(days=7)).strftime('%Y-%m-%d')
            for j in range(1, len(df)): # row TIME 
                t = df.iloc[j][0].split(' - ')
                self.cursor.execute("INSERT INTO " + tname + "(DateTime, Room, Module) VALUES('%s', '%s', '%s')" % (pd.to_datetime(date + ' ' + datetime.strptime(t[0], "%H:%M").strftime('%H:%M:%S')), room, df.iloc[j][i]))
                self.con.commit()           
        return
    
    def addModule(self, tname, df, room): 
        # Insert data for Module and Num registered
        for i in range(1, 10, 2): # column DATE
            for j in range(1, len(df)): # row TIME
                # 'INSERT IGNORE' makes sure that there are no duplicate rows
                self.cursor.execute("INSERT IGNORE INTO " + tname + " (ModuleName, NumReg) VALUES('%s', %d)" 
                                    % (df.iloc[j][i], df.iloc[j][i+1] if df.iloc[j][i+1] else 0))
                self.con.commit()
        return
    
    
    def timetableTable(self, tname, df):     
        for i in range(1, len(df)): # i is row, other column
            self.cursor.execute("INSERT INTO " + tname + "(Time, Monday_Module, Monday_NumReg, Tuesday_Module, Tuesday_NumReg, Wednesday_Module, Wednesday_NumReg, Thursday_Module, Thursday_NumReg, Friday_Module, Friday_NumReg) VALUES('%s', '%s', %d, '%s', %d,'%s', %d, '%s', %d, '%s', %d)" % 
            (df.iloc[i][0], # Time
             df.iloc[i][1], # Monday
             df.iloc[i][2] if df.iloc[i][2] else 0, # Number registered
             df.iloc[i][3], # Tuesday...
             df.iloc[i][4] if df.iloc[i][4] else 0,
             df.iloc[i][5],
             df.iloc[i][6] if df.iloc[i][6] else 0,
             df.iloc[i][7],
             df.iloc[i][8] if df.iloc[i][8] else 0, 
             df.iloc[i][9], 
             df.iloc[i][10] if df.iloc[i][10] else 0))
            self.con.commit()           
        return

# Connect to database
name = 'MainDatabase'

# Create timetable object
data = timetable(name)
# Create table with modules and time they're on
tnameT = 'TimeModule'
data.createTableTimeModule(tnameT)
# Create Modules table
tnameM = 'Modules'
data.createTableModule(tnameM)


# Create empty dictionary to hold room title and capacity
rooms = {}

###### B002 #####
# Read timetable info for B-002
room = 'B-002'
df = pd.read_excel('B0.02 B0.03 B0.04 Timetable.xlsx', sheetname='B0.02')
df = df.iloc[:10,:11]
# Replace all null values with 'None'
df = df.astype(object).where(pd.notnull(df), None)
# Fix - Rename lectures and practicals
df = data.fixLecPrac(df)

##### B002 - TIME & MODULE #####
# Add timetable data for week 1
data.addTimeModuleWk1(tnameT, df, room)
# Add timetable data for week 2 - timetable is the same, only difference is the dates
data.addTimeModuleWk2(tnameT, df, room)

# read the capacity of the room 'Room capacity: 90'
# split the cell containing the capacity
cap = df.columns[2].split()
# Add room and its capacity to dictionary
rooms[room] = cap[2]

##### B002 - MODULE #####
# Add Modules and Number registered for each module a Modules table
data.addModule(tnameM, df, room)

##### B002 - Timetable #####
# Create Timetable table for B002 and add data
tnameTT = 'B002'
data.createTableTimetable(tnameTT)
data.timetableTable(tnameTT, df)

###### B003 #####
# Read timetable info for B-003
room = 'B-003'
df = pd.read_excel('B0.02 B0.03 B0.04 Timetable.xlsx', sheetname='B0.03')
df = df.iloc[:10,:11]
# Replace all null values with 'None'
df = df.astype(object).where(pd.notnull(df), None)
# Fix (rename practicals)
df = data.fixLecPrac(df)

##### B003 - TIME & MODULE #####
data.addTimeModuleWk1(tnameT, df, room)
# Add timetable data for week 2 - timetable is the same, only difference is the dates
data.addTimeModuleWk2(tnameT, df, room)

# read the capacity of the room e.g.'Room capacity: 90'
# split the cell containing the capacity
cap = df.columns[2].split()
# Add room and its capacity to dictionary 'rooms'
rooms[room] = cap[2]

##### B003 - MODULE #####
# Add Modules and Number registered for each module a Modules table
data.addModule(tnameM, df, room)

##### B003 - Timetable #####
# Create Timetable table for B003 and add data
tnameTT = 'B003'
data.createTableTimetable(tnameTT)
data.timetableTable(tnameTT, df)

###### B004 #####
# Read timetable info for B-004
room = 'B-004'
df = pd.read_excel('B0.02 B0.03 B0.04 Timetable.xlsx', sheetname='B0.04')
df = df.iloc[:10,12:23]
# Replace all null values with 'None'
df = df.astype(object).where(pd.notnull(df), None)
# Fix (rename practicals)
df = data.fixLecPrac(df)

##### B004 - TIME & MODULE #####
# Add timetable data for week 1
data.addTimeModuleWk1(tnameT, df, room)
# Add timetable data for week 2 - timetable is the same, only difference is the dates
data.addTimeModuleWk2(tnameT, df, room)

# read the capacity of the room 'Room capacity: 90'
# split the cell containing the capacity
cap = df.columns[2].split()
# Add room and its capacity to dictionary
rooms[room] = cap[2]

##### B004 - MODULE #####
# Add Modules and Number registered for each module to Modules table
data.addModule(tnameM, df, room)

##### B004 - Timetable #####
# Create Timetable table for B004 and add data WK2
tnameTT = 'B004_WK2'
data.createTableTimetable(tnameTT)
data.timetableTable(tnameTT, df)

# Create Timetable table for B002 and add data WK1
tnameTT = 'B004_WK1'
df = pd.read_excel('B0.02 B0.03 B0.04 Timetable.xlsx', sheetname='B0.04')
df = df.iloc[:10,:11]
df = df.astype(object).where(pd.notnull(df), None)
# Fix (Rename Practicals)
df = data.fixLecPrac(df)
data.createTableTimetable(tnameTT)
data.timetableTable(tnameTT, df)

# ROOM TABLE
# Connect to Database
name = "MainDatabase"
con = db.connect(host="localhost", user="root", passwd='', db=name)
cursor = con.cursor()

# Create table
sql = """CREATE TABLE IF NOT EXISTS Rooms (Room VARCHAR(10), Capacity FLOAT, PRIMARY KEY(Room))"""
cursor.execute(sql)

# Insert rooms and capacity containined in 'rooms' dictionary into table 
for key, value in rooms.items():
    cursor.execute("INSERT INTO Rooms (Room, Capacity) VALUES ('%s', %f)" % (key, float(value)))
    con.commit()