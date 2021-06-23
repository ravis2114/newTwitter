import mysql.connector

conn = mysql.connector.connect(host='freedb.tech',user='freedbtech_rsyst', password='zxcvbnml', database='freedbtech_rsyst')
cursor = conn.cursor()


cursor.execute(("SELECT * FROM newtwitter_user WHERE userid='{}'".format('ravi123')))
user = cursor.fetchall()

print(user)
print(len(user))

print(user[0][1])

if user:
    print('user exists')
else:
    print('user not found')