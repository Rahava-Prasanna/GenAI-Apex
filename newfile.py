import sqlite3
connection = sqlite3.connect("Students.db")

cursor = connection.cursor()
cursor.execute("""CREATE table Students(NAME varchar(20),CLASS varchar(20),SECTION varchar(20),MARK INT""")

#insert values into table

cursor.execute("""INSERT into students values("Rohan","Data science","B",80)""")
cursor.execute("""INSERT into students values("Dinesh","Data science","A",90)""")
cursor.execute("""INSERT into students values("Jonathan","AI","C",90)""")
cursor.execute("""INSERT into students values("Tony Stark","Web Dev","B",87)""")
print("The inserted records are")

res = cursor.execute(""" select * from Students""")
for i in res:
    print(i)