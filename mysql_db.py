import pymysql

conn = pymysql.connect(user='root',password='welcome$1234',host='127.0.0.1',database='TEST_PYTHON_SQL')
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS TEST_PYTHON_SQL")

sql_query='''CREATE TABLE IF NOT EXISTS  
               Players (id INT AUTO_INCREMENT PRIMARY KEY , 
                          Name VARCHAR(255), 
                          Country VARCHAR(255),
                          IPL_team VARCHAR(255))'''

cursor.execute(sql_query)
cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

cursor.close()
conn.close()