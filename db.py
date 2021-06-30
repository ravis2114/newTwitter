import mysql.connector

conn = mysql.connector.connect(host='freedb.tech',user='freedbtech_rsyst', password='zxcvbnml', database='freedbtech_rsyst')
cursor = conn.cursor()

# qry=" DELETE FROM newtwitter_comment where userid='doge' "
qry="SELECT * from newtwitter_comment"
cursor.execute((qry))
fetch = cursor.fetchall()
print(fetch)


