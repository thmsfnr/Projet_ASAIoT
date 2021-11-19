import mysql.connector

class DB:

   database = mysql.connector.connect(host="localhost", user="root", password="root", database="Backdel") # Database connection informations
   cursor = database.cursor() # Connection to the database

   def init(self):
      """Initialisation of the database"""

      self.createTables(self)

   def createTables(self):
      """Creation of the database tables"""

      self.cursor.execute("""
         CREATE TABLE IF NOT EXISTS Trace (
         idTrace int(6) NOT NULL AUTO_INCREMENT,
         nomTrace varchar(100) DEFAULT NULL,
         PRIMARY KEY(idTrace)
         );
      """)

      self.cursor.execute("""
         CREATE TABLE IF NOT EXISTS Data (
         idData int(6) NOT NULL AUTO_INCREMENT,
         idTrace int(6) DEFAULT NULL,
         latitude float(20) DEFAULT NULL,
         longitude float(20) DEFAULT NULL,
         PRIMARY KEY(idData),
         FOREIGN KEY(idTrace) REFERENCES Trace(idTrace)
         );
      """)

   def insertTrace(self,nameTrace):
      """Insert a trace in the database"""

      self.cursor.execute("""
         INSERT INTO Trace(nomTrace) 
         VALUES (?);"""
         , (nameTrace)
      )

      self.cursor.commit()

   def insertData(self,idTrace,latitude,longitude):
      """Insert data of trace in the database"""

      self.cursor.execute("""
         INSERT INTO Data(idTrace,latitude,longitude) 
         VALUES (?);"""
         , (idTrace,latitude,longitude)
      )

      self.cursor.commit()

   def selectTraceWithName(self,nameTrace):
      """Select a trace by its name"""
      
      self.cursor.execute("""
         SELECT idTrace 
         FROM Trace
         WHERE nomTrace='%s';"""
         % (nameTrace)
      )
      return self.cursor.fetchone()

   def selectDataWithIdTrace(self,idTrace):
      """Select trace data with its id"""
       
      self.cursor.execute("""
         SELECT Data.latitude,Data.longitude 
         FROM Data
         INNER JOIN Trace 
         ON Trace.idTrace = Data.idTrace
         WHERE Trace.idTrace='%s'
         ORDER BY Data.idData;"""
         % (idTrace)
      )
      return self.cursor.fetchall()

   def selectAllIdTrace(self):
      """Select all id of trace"""

      self.cursor.execute("""
         SELECT idTrace
         FROM Trace 
         ;"""
      )
      return self.cursor.fetch()

   def close(self):
      """Close interactions with the database"""

      self.database.close()


  