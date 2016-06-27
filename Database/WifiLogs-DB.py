import pandas as pd
import MySQLdb as db
from datetime import datetime
import os

# table class 
class data():
    def __init__(self, name):
        self.con = db.connect(host="localhost", user="root", passwd='', db=name)
        self.cursor = self.con.cursor()
        
    def createTable(self, tname):
        sql = "CREATE TABLE IF NOT EXISTS " + tname + " (Campus VARCHAR(30), Building VARCHAR(40), Room VARCHAR(20), DateTime datetime, Associated int, Authenticated int)"
        self.cursor.execute(sql)
        
    def openFile(self, tname, fname):
        with open(fname) as f:
            for num, line in enumerate(f,1):
                if line.startswith('Key'):
                    break
        df = pd.read_csv(fname, skiprows=num-1)
        return df
    
    def fixFile(self, df):
        for i in range(0, len(df)):
            df['Event Time'][i] = df['Event Time'][i].replace('GMT+00:00','')
            df['Event Time'][i] = datetime.strptime(df['Event Time'][i], '%a %b %d %X %Y')
            df['Key'][i] = df['Key'][i].split(' > ')
        return df
        
    def addFile(self, tname, df):     
        for i in range(0, len(df)):
            self.cursor.execute("INSERT INTO " + tname + "(Campus, Building, Room, DateTime, Associated, Authenticated) VALUES('%s', '%s', '%s', '%s', %d, %d)" % (df['Key'][i][0], df['Key'][i][1], df['Key'][i][2], df['Event Time'][i], df['Associated Client Count'][i], df['Authenticated Client Count'][i]))
            self.con.commit()           
        return


name = 'WiFiData'
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

# DATETIME - format: YYYY-MM-DD HH:MI:SS.