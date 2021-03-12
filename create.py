
import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")

conn.execute("""CREATE TABLE person
         (sno INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         city           TEXT     NOT NULL)""");
print("Table created successfully")

conn.close()