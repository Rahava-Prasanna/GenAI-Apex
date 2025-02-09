import sqlite3
connection = sqlite3.connect("employee.db")

cursor = connection.cursor()
cursor.execute("""create table emptab(empid int,empname varchar(20),empsalary int,empdesig varchar(20))""")

#insert values into table

cursor.execute("""insert into emptab values(1,"rahav",80000,"project lead")""")
cursor.execute("""insert into emptab values(2,"dinesh",70000,"data scientist")""")
cursor.execute("""insert into emptab values(3,"aditya",60000,"frontend dev")""")
cursor.execute("""insert into emptab values(4,"gokul",50000,"powerbi analyst")""")

res = cursor.execute(""" select * from emptab""")
for i in res:
    print(i)