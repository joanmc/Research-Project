import pandas as pd
import MySQLdb as db
from datetime import datetime
import os

# DATETIME format: YYYY-MM-DD HH:MI:SS.

# table class 
class data():
    def __init__(self, name):
        # Connect to Database
        self.con = db.connect(host="localhost", user="root", passwd='', db=name)
        self.cursor = self.con.cursor()
        
    def createTable(self, tname):
        # Create a table
        sql = "CREATE TABLE " + tname + " (DateTime datetime, Room VARCHAR(20), Associated int, Authenticated int, PRIMARY KEY(DateTime, Room), FOREIGN KEY (Room) REFERENCES Rooms(Room))"
        self.cursor.execute(sql)
        
    def openFile(self, tname, fname):
        # Find keyworrd 'key' in csv file and read into data frame from there
        with open(fname) as f:
            # f is the file name, starting on row 1
            # Accounts for csvs where 'key' is in a different row
            # num = counter
            for num, line in enumerate(f,1):
                if line.startswith('Key'):
                    break
        df = pd.read_csv(fname, skiprows=num-1)
        return df
    
    def fixFile(self, df):
        for i in range(0, len(df)):
            # put time into sql format
            df['Event Time'][i] = df['Event Time'][i].replace('GMT+00:00','')
            df['Event Time'][i] = datetime.strptime(df['Event Time'][i], '%a %b %d %X %Y')
            # Split column Key (contains campus, building and room) into separate parts so they can be added to separate columns of database table
            df['Key'][i] = df['Key'][i].split(' > ')
        return df
        

    def addFile(self, tname, df):
        # put data from dataframe into table in database
        for i in range(0, len(df)):
            self.cursor.execute("INSERT INTO " + tname + "(Room, DateTime, Associated, Authenticated) VALUES('%s', '%s', %d, %d)" 
                                % (df['Key'][i][2], df['Event Time'][i], df['Associated Client Count'][i], 
                                 df['Authenticated Client Count'][i]))
            self.con.commit()           
        return


name = 'DatabaseMain'
myData = data(name)
tname = 'WiFiLogData'
myData.createTable(tname)

path = '/Users/JoanMcCarthy/Google Drive/Computer Science/Research Practicum/Data/CSI WifiLogs'

for fn in os.listdir(path):
    if fn.lower().endswith('.csv'):
        #print "File Name: " + fn
        fname = os.path.join(path, fn)
        df = myData.openFile(tname, fname)
        df = myData.fixFile(df)
        myData.addFile(tname, df)