import pymysql

conn = pymysql.connect(user='root', password='welcome$1234', host='127.0.0.1', database='TEST_PYMYSQL')
cursor = conn.cursor()

# cursor.execute("CREATE DATABASE IF NOT EXISTS TEST_PYMYSQL")
# cursor.execute("USE TEST_PYMYSQL")
#
# sql_query='''CREATE TABLE IF NOT EXISTS
#                EMP1 (id INT AUTO_INCREMENT PRIMARY KEY ,
#                        name varchar(50),
#                         age int,
#                         address varchar(100),
#                         salary decimal(10,2));'''
# cursor.execute(sql_query)

#to insert the records in table
def insert_pymysql(name,age,address,salary):
    sql_query = f"insert into emp1(Name,age,address,salary) values ('{name}','{age}','{address}','{salary}')"
    cursor.execute(sql_query)
    conn.commit()
    print(sql_query)

n = int(input('how many rows : '))
for i in range(n):
    name = input('Enter name : ')
    age = input('Enter age : ')
    address = input('Enter address : ')
    salary = input('Enter salary :')

    insert_pymysql(name,age,address,salary)

#to view the results in table
cursor.execute("select * from emp1")
while True:
    row = cursor.fetchone()
    if row is not None:
        print(row)
    else:
        break

cursor.close()
conn.close()