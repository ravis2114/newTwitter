from blueprints.landingPage.views import dashboard
from flask import Blueprint, render_template, session, redirect, url_for, request
import datetime
import mysql.connector
import dropbox

dropbox_access_token= "xogv50OrMysAAAAAAAAAAZLNZRmAmZXik0U4xaF6EoWmQlFMPiDuw6JmfxzDWTiF"
dropbox_path= "/Apps/newTwitter"
dbx = dropbox.Dropbox(dropbox_access_token)

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
		time = datetime.datetime.now()

		if 'tweetArea' in request.form:
			post = request.form['tweetArea']
			cursor.execute(("INSERT INTO newtwitter_comment (userid, comments, toc) VALUES ('{}','{}','{}')".format(userid,post,time)))
			conn.commit()
		if 'dp' in request.files:
			dp = request.files['dp']
			dp.save(f'static/images/{userid}.jpg')
			im_dp = open(f'static/images/{userid}.jpg', 'rb').read()
			dbx.files_upload(im_dp, f'/{userid}dp.jpg')
		if 'cover' in request.files:
			cover = request.files['cover']
			cover.save(f'static/images/{userid}.jpg')
			im_cover = open(f'static/images/{userid}.jpg', 'rb').read()
			dbx.files_upload(im_cover, f'/{userid}cover.jpg')
		
		return redirect(url_for('landingPage.dashboard'))
	return redirect(url_for('landingPage.dashboard'))

		# #getting user info
		# cursor.execute(("SELECT * FROM newtwitter_user WHERE userid='{}'".format(userid)))
		# global user
		# user = cursor.fetchall()

		# #getting all the posts
		# cursor.execute(("SELECT * FROM newtwitter_comment WHERE userid='{}' ORDER BY toc DESC".format(userid)))
		# global comments
		# comments = cursor.fetchall()

		# return render_template('dashBoard/profile.html', data=(user,comments))
		