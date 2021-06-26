import mysql.connector

conn = mysql.connector.connect(host='freedb.tech',user='freedbtech_rsyst', password='zxcvbnml', database='freedbtech_rsyst')
cursor = conn.cursor()

qry=" SELECT * FROM newtwitter_comment where userid='test2' "
cursor.execute((qry))
comments = cursor.fetchall()

print(comments)

