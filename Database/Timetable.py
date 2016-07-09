import pandas as pd
import xlrd
import MySQLdb as db
from dateutil.parser import parse
from datetime import datetime
from datetime import timedelta

class timetable():
    def __init__(self, name):
        # connect to the database
        self.con = db.connect(host="localhost", user="root", passwd='', db=name)
        self.cursor = self.con.cursor()
        
    def createTableTimeModule(self, tname):
        # create table with modules and the time
        sql = "CREATE TABLE IF NOT EXISTS " + tname + " (DateTime datetime, Room VARCHAR(10), Module VARCHAR(30) NOT NULL, PRIMARY KEY (DateTime, Room), FOREIGN KEY (Room) REFERENCES Rooms(Room), FOREIGN KEY (Module) REFERENCES Modules(ModuleName))"
        self.cursor.execute(sql)
        
    def createTableModule(self, tname):
        # Create Modules table
        sql = "CREATE TABLE IF NOT EXISTS " + tname + " (ModuleName VARCHAR(30), NumReg INT, PRIMARY KEY(ModuleName))"
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


# Connect to database
name = 'DatabaseMain'
# Create timetable object
data = timetable(name)

# Create empty dictionary to hold room title and capacity
rooms = {}

###### B002 #####
# Read timetable info for B-002
room = 'B-002'
df_b002 = pd.read_excel('B0.02 B0.03 B0.04 Timetable.xlsx', sheetname='B0.02')
df_b002 = df_b002.iloc[:10,:11]
# Replace all null values with 'None'
df_b002 = df_b002.astype(object).where(pd.notnull(df_b002), None)
# Fix - Rename lectures and practicals
df_b002 = data.fixLecPrac(df_b002)
# read the capacity of the room 'Room capacity: 90'
# split the cell containing the capacity
cap = df_b002.columns[2].split()
# Add room and its capacity to dictionary
rooms[room] = cap[2]

###### B003 #####
# Read timetable info for B-003
room = 'B-003'
df_b003 = pd.read_excel('B0.02 B0.03 B0.04 Timetable.xlsx', sheetname='B0.03')
df_b003 = df_b003.iloc[:10,:11]
# Replace all null values with 'None'
df_b003 = df_b003.astype(object).where(pd.notnull(df), None)
# Fix (rename practicals)
df_b003 = data.fixLecPrac(df_b003)
# read the capacity of the room e.g.'Room capacity: 90'
# split the cell containing the capacity
cap = df_b003.columns[2].split()
# Add room and its capacity to dictionary 'rooms'
rooms[room] = cap[2]

###### B004 #####
# Read timetable info for B-004
room = 'B-004'
df_b004 = pd.read_excel('B0.02 B0.03 B0.04 Timetable.xlsx', sheetname='B0.04')
df_b004 = df_b004.iloc[:10,12:23]
# Replace all null values with 'None'
df_b004 = df.astype(object).where(pd.notnull(df_b004), None)
# Fix (rename practicals)
df_b004 = data.fixLecPrac(df_b004)
# read the capacity of the room 'Room capacity: 90'
# split the cell containing the capacity
cap = df_b004.columns[2].split()
# Add room and its capacity to dictionary
rooms[room] = cap[2]

# ROOM TABLE
# Connect to Database
name = "DatabaseMain"
con = db.connect(host="localhost", user="root", passwd='', db=name)
cursor = con.cursor()

# Create table
sql = """CREATE TABLE IF NOT EXISTS Rooms (Room VARCHAR(10), Building VARCHAR(30), Campus VARCHAR(30), Capacity INT, PRIMARY KEY(Room))"""
cursor.execute(sql)

campus = 'Belfield'
building = 'Computer Science'

# Insert rooms and capacity containined in 'rooms' dictionary into table 
for key, value in rooms.items():
    cursor.execute("INSERT INTO Rooms (Room, Building, Campus, Capacity) VALUES ('%s', '%s', '%s', %d)" % (key, building, campus, int(float(value))))
    con.commit()

# MODULES TABLE
tnameM = 'Modules'
data.createTableModule(tnameM)

##### B002 - MODULE #####
# Add Modules and Number registered for each module a Modules table
data.addModule(tnameM, df_b002, room)

#### B003 - MODULE #####
# Add Modules and Number registered for each module a Modules table
data.addModule(tnameM, df_b003, room)

#### B004 - MODULE #####
# Add Modules and Number registered for each module to Modules table
data.addModule(tnameM, df_b004, room)

# TIMEMODULE TABLE
tnameT = 'TimeModule'
data.createTableTimeModule(tnameT)

##### B002 - TIME & MODULE #####
# Add timetable data for week 1
data.addTimeModuleWk1(tnameT, df_b002, room)
# Add timetable data for week 2 - timetable is the same, only difference is the dates
data.addTimeModuleWk2(tnameT, df_b002, room)

##### B003 - TIME & MODULE #####
# Add timetable data for week 1
data.addTimeModuleWk1(tnameT, df_b003, room)
# Add timetable data for week 2 - timetable is the same, only difference is the dates
data.addTimeModuleWk2(tnameT, df_b003, room)

##### B004 - TIME & MODULE #####
# Add timetable data for week 1
data.addTimeModuleWk1(tnameT, df_b004, room)
# Add timetable data for week 2 - timetable is the same, only difference is the dates
data.addTimeModuleWk2(tnameT, df_b004, room)

