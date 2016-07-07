import MySQLdb as db

# Connect to database
name = "MainDatabase"
con = db.connect(host="localhost", user="root", passwd='', db=name)
cursor = con.cursor()

# Combine Timetable, Wifi Average and Ground Truth Data
sql ="""CREATE TABLE IF NOT EXISTS CombinedData
            SELECT A.DateTime, A.Room, T.Module, A.AvgNumWifiConn, G.GroundTruth
            FROM AverageNumWifiConnections A, TimeModule T
            LEFT JOIN GroundTruth_Percentage G
            ON T.DateTime = G.DateTime AND T.Room = G.Room
            WHERE T.DateTime = A.DateTime AND T.Room = A.Room"""
cursor.execute(sql)

# Foreign Key - Module
sql = """ALTER TABLE CombinedData
            ADD FOREIGN KEY (Module)
            REFERENCES Modules(ModuleName)"""
cursor.execute(sql)

# Foreign key - room
sql = """ALTER TABLE CombinedData
            ADD FOREIGN KEY (Room)
            REFERENCES Rooms(Room)"""
cursor.execute(sql)