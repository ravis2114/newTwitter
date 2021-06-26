from blueprints.landingPage.views import dashboard
from flask import Blueprint, render_template, session, redirect, url_for, request
import datetime
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
        print(userid)
        post = request.form['tweetArea']
        time = datetime.datetime.now()

        cursor.execute(("INSERT INTO newtwitter_comment (userid, comments, toc) VALUES ('{}','{}','{}')".format(userid,post,time)))
        conn.commit()

        return render_template('dashBoard/profile.html')