import pymysql

conn = pymysql.connect(user='root', password='welcome$1234', host='127.0.0.1', database='TEST_PYTHON_SQL')
cursor = conn.cursor()

print("----------ReAd Data--------------")

cursor.execute("select * from players")

while True:
    row = cursor.fetchone()
    if row is not None:
        print(row)
    else:
        break

cursor.close()
conn.close()