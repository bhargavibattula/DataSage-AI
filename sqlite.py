from sqlite3 import Connection
import sqlite3

connection = sqlite3.connect("data.db")
### create a cursor object 
cursor = connection.cursor()

table_info = """
create table STUDENT(NAME VARCHAR(25) , CLASS VARCHAR(25) , SECTION VARCHAR(25) , MARKS INT)
"""

cursor.execute(table_info)

cursor.execute("INSERT INTO STUDENT VALUES ('Rahul', '10', 'A', 85)")
cursor.execute("INSERT INTO STUDENT VALUES ('Anjali', '10', 'A', 92)")
cursor.execute("INSERT INTO STUDENT VALUES ('Kiran', '10', 'B', 76)")
cursor.execute("INSERT INTO STUDENT VALUES ('Sneha', '10', 'B', 89)")
cursor.execute("INSERT INTO STUDENT VALUES ('Arjun', '9', 'A', 67)")
cursor.execute("INSERT INTO STUDENT VALUES ('Pooja', '9', 'A', 74)")
cursor.execute("INSERT INTO STUDENT VALUES ('Vikram', '9', 'B', 81)")
cursor.execute("INSERT INTO STUDENT VALUES ('Divya', '9', 'B', 95)")
cursor.execute("INSERT INTO STUDENT VALUES ('Ravi', '8', 'A', 58)")
cursor.execute("INSERT INTO STUDENT VALUES ('Meena', '8', 'A', 64)")
cursor.execute("INSERT INTO STUDENT VALUES ('Suresh', '8', 'B', 72)")
cursor.execute("INSERT INTO STUDENT VALUES ('Lakshmi', '8', 'B', 88)")

## display all the records
print("The inserted records are")
data = cursor.execute("SELECT * FROM STUDENT")

for row in data:
    print(row)



print("table created successfully")

connection.commit()
connection.close()
