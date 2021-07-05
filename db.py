import mysql.connector

conn = mysql.connector.connect(host='freedb.tech',user='freedbtech_rsyst', password='zxcvbnml', database='freedbtech_rsyst')
cursor = conn.cursor()

# qry=" DELETE FROM newtwitter_comment where userid='doge' "
# qry="create table twitter_user ( bio varchar(500), location varchar(25), )"
# cursor.execute((qry))
# fetch = cursor.fetchall()
# print(fetch)

cursor.execute(("SELECT * FROM newtwitter_user WHERE userid='{}' ".format('ravi123')))
comments = cursor.fetchall()
print(comments)
