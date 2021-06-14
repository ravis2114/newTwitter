import mysql.connector

conn = mysql.connector.connect(host='remotemysql.com',user='kEOWWtr4ag', password='dgXWQcifF8', database='kEOWWtr4ag')
cursor = conn.cursor()

cursor.execute(('select * from users'))
xx = cursor.fetchall()
print(xx, type(xx))
for i in xx:
    print(i)