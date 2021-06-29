from blueprints.landingPage.views import dashboard
from flask import Blueprint, render_template, session, redirect, url_for, request
import datetime
import io
import base64
from PIL import Image
import mysql.connector

conn = mysql.connector.connect(host='freedb.tech',user='freedbtech_rsyst', password='zxcvbnml', database='freedbtech_rsyst')
cursor = conn.cursor()

dashBoard = Blueprint('dashBoard',__name__, template_folder='templates', static_folder='static',static_url_path='dashBoard/static')

@dashBoard.route('/', methods=['POST', 'GET'])
def home():
    return render_template('dashBoard/profile.html')

@dashBoard.route('/post', methods=['GET', 'POST'])
def post():
    if request.method=='POST':
        userid = session['user']
        print(userid, session)
        post = request.form['tweetArea']
        print(post)
        time = datetime.datetime.now()

        cursor.execute(("SELECT * FROM newtwitter_user WHERE userid='{}'".format(userid)))
        global user
        user = cursor.fetchall()


        if post:
            cursor.execute(("INSERT INTO newtwitter_comment (userid, comments, toc) VALUES ('{}','{}','{}')".format(userid,post,time)))
            conn.commit()

        cursor.execute(("SELECT * FROM newtwitter_comment WHERE userid='{}' ORDER BY toc DESC".format(userid)))
        global comments
        comments = cursor.fetchall()
        # print(comments)

        return render_template('dashBoard/profile.html', data=(user,comments))

@dashBoard.route('/upload', methods=['GET', 'POST'])
def xxx():
    if request.method=='POST':
        im = request.files['image']
        im=im.save('static/images/x.jpg')
        return render_template('dashBoard/demo.html')
    else:
        return render_template('dashBoard/demo.html')