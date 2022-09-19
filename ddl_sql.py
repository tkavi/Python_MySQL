import pymysql

conn = pymysql.connect(user='root', password='welcome$1234', host='127.0.0.1', database='TEST_PYTHON_SQL')
cursor = conn.cursor()

# cursor.execute("DESCRIBE players")
#
# #to fetch and print the metadata of the table
# indexlist = cursor.fetchall()
# for i in indexlist:
#     print(i)
# # conn.commit()

#cursor.execute("ALTER table players ADD role varchar(25)")
#cursor.execute("ALTER table players RENAME COLUMN role TO Speciality")

cursor.close()
conn.close()