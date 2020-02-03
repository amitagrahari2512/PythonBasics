import mysql.connector
print("First We need to install mysql-connector in pycharm or via pip")

mydb = mysql.connector.connect(host="localhost", user ="root", password="root")

print("If we want to any data fetch from database we need to use execute(query) method"
      "and all data from backend is store in cursor so we can iterate those cursor and get values")

myCursor = mydb.cursor()
myCursor.execute("show databases")

for dbName in myCursor:
    print(dbName)


print("When we want to get data from table , then we need to pass database name also")

mydb = mysql.connector.connect(host="localhost", user ="root", password="root",database = 'pythoncode')

myCursor = mydb.cursor()
myCursor.execute("select * from student")

print("\n")
print("we can get data directly from cursor")
for student in myCursor:
    print(student)

print("\n")
print("we can get data from cursor using fetchall() method")

myCursor = mydb.cursor()
myCursor.execute("select * from student")
result = myCursor.fetchall()

for student in result:
    print(student)

print("\n")
print("we can get only one data using fetchone() method")
myCursor = mydb.cursor()
myCursor.execute("select * from student")

result = myCursor.fetchone()
print(result)

