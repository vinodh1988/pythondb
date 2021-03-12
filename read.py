import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")



conn.execute("insert into person(sno,name,city) values(?,?,?)",(1,'Ram','Chennai'))

conn.execute("insert into person(sno,name,city) values(?,?,?)",(2,'Jay','Chennai'))

conn.execute("insert into person(sno,name,city) values(?,?,?)",(3,'Harry','Chennai'))

cursor=conn.execute("select * from person")

for row in cursor:
    print("{} {} {}".format(row[0],row[1],row[2]))

    #alchemy