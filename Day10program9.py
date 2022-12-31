import sqlite3 as lite
con=lite.connect('mtica.db')
cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS cars ")
cur.execute(''' CREATE TABLE cars(
       Id INT,Name TEXT,price INT)''')
print("table cars created.")
cur.execute("INSERT INTO cars VALUES(1,'Audi',456783)")
cur.execute("INSERT INTO cars VALUES(2,'Mercedes',57127)")
cur.execute("INSERT INTO cars VALUES(3,'Skoda',76534)")
cur.execute("INSERT INTO cars VALUES(4,'Volvo',556783)")
cur.execute("INSERT INTO cars VALUES(5,'Bentley',35600)")
con.commit()
print("values in table car inserted.")
