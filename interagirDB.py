import mysql.connector
conn = mysql.connector.connect(host="localhost",
                               user="root", password="root", 
                               database="Backdel")
cursor = conn.cursor()

# Operations a realiser sur la base ...
cursor.execute("""
   CREATE TABLE IF NOT EXISTS Produits (
      ref int(6) NOT NULL,
      nom varchar(100) DEFAULT NULL,
      stock int(4) DEFAULT NULL,
      prix float(5,2) DEFAULT NULL,
      PRIMARY KEY(ref),
      CHECK (stock>=0)
      );
""")

conn.close()