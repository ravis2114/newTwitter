from blueprints.landingPage.views import dashboard
from flask import Blueprint, render_template, session, redirect, url_for, request
import datetime
import os
import mysql.connector
# import dropbox

# dropbox_access_token= "xogv50OrMysAAAAAAAAAAZLNZRmAmZXik0U4xaF6EoWmQlFMPiDuw6JmfxzDWTiF"
# dropbox_path= "/Apps/newTwitter"
# dbx = dropbox.Dropbox(dropbox_access_token)

import boto3
from blueprints.dashBoard.amazon_config import access_key, secret_access_key
s3 = boto3.resource(
    service_name='s3',
    region_name='ap-south-1',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_access_key
)

# conn = mysql.connector.connect(host='freedb.tech',user='freedbtech_rsyst', password='zxcvbnml', database='freedbtech_rsyst')
# cursor = conn.cursor()

dashBoard = Blueprint('dashBoard',__name__, template_folder='templates', static_folder='static',static_url_path='dashBoard/static')

@dashBoard.route('/', methods=['POST', 'GET'])
def home():
	return render_template('dashBoard/profile.html')

@dashBoard.route('/post', methods=['GET', 'POST'])
def post():
	if request.method=='POST':
		userid = session['user']

		if request.form.get('changeBio', False):
			bio=request.form['changeBio']
			conn = mysql.connector.connect(host='database-404.cljpc2llv9ft.ap-south-1.rds.amazonaws.com',user='admin', password='admin2114', database='newtwitter')
			cursor = conn.cursor()
			cursor.execute(("UPDATE newtwitter_user SET bio='{}' WHERE userid='{}' ".format(bio, userid)))
			conn.commit()
		if request.form.get('loc', False):
			loc=request.form['loc']
			conn = mysql.connector.connect(host='database-404.cljpc2llv9ft.ap-south-1.rds.amazonaws.com',user='admin', password='admin2114', database='newtwitter')
			cursor = conn.cursor()
			cursor.execute(("UPDATE newtwitter_user SET location='{}' WHERE userid='{}' ".format(loc, userid)))
			conn.commit()
		if request.form.get('uname', False):
			uname=request.form['uname']
			conn = mysql.connector.connect(host='database-404.cljpc2llv9ft.ap-south-1.rds.amazonaws.com',user='admin', password='admin2114', database='newtwitter')
			cursor = conn.cursor()
			cursor.execute(("UPDATE newtwitter_user SET username='{}' WHERE userid='{}' ".format(uname, userid)))
			conn.commit()
		if request.form.get('linkbio', False):
			linkbio=request.form['linkbio']
			conn = mysql.connector.connect(host='database-404.cljpc2llv9ft.ap-south-1.rds.amazonaws.com',user='admin', password='admin2114', database='newtwitter')
			cursor = conn.cursor()
			cursor.execute(("UPDATE newtwitter_user SET ext_link='{}' WHERE userid='{}' ".format(linkbio, userid)))
			conn.commit()

		# if 'tweetArea' in request.form:
		# 	post = request.form['tweetArea']
		# 	cursor.execute(("INSERT INTO newtwitter_comment (userid, comments, toc) VALUES ('{}','{}','{}')".format(userid,post,time)))
		# 	conn.commit()
		if request.files.get('dp', False):
			dp = request.files['dp']
			dp.save(f'static/images/{userid}dp.jpg')
			# im_dp = open(f'static/images/{userid}.jpg', 'rb').read()
			# dbx.files_upload(im_dp, f'/{userid}dp.jpg', mode=dropbox.files.WriteMode.overwrite)
			s3.Bucket('newtwitter-bucket').upload_file(f'static/images/{userid}dp.jpg', f'images/{userid}dp.jpg', {'ACL':'public-read'})
			os.remove(f'static/images/{userid}dp.jpg')
			#get link to save in user table
			# dp = dbx.files_get_temporary_link(f'/{userid}dp.jpg')
			# dp =dp.link
			dp = f'https://newtwitter-bucket.s3.ap-south-1.amazonaws.com/images/{userid}dp.jpg'
			conn = mysql.connector.connect(host='database-404.cljpc2llv9ft.ap-south-1.rds.amazonaws.com',user='admin', password='admin2114', database='newtwitter')
			cursor = conn.cursor()
			cursor.execute(("UPDATE newtwitter_user SET dp_link='{}' WHERE userid='{}' ".format(dp, userid)))
			conn.commit()


		if request.files.get('cover', False):
			cover = request.files['cover']
			cover.save(f'static/images/{userid}cover.jpg')
			# im_cover = open(f'static/images/{userid}.jpg', 'rb').read()
			# dbx.files_upload(im_cover, f'/{userid}cover.jpg', mode=dropbox.files.WriteMode.overwrite)
			s3.Bucket('newtwitter-bucket').upload_file(f'static/images/{userid}cover.jpg', f'images/{userid}cover.jpg', {'ACL':'public-read'})
			os.remove(f'static/images/{userid}cover.jpg')

			cover = f'https://newtwitter-bucket.s3.ap-south-1.amazonaws.com/images/{userid}cover.jpg'
			conn = mysql.connector.connect(host='database-404.cljpc2llv9ft.ap-south-1.rds.amazonaws.com',user='admin', password='admin2114', database='newtwitter')
			cursor = conn.cursor()
			cursor.execute(("UPDATE newtwitter_user SET cover_link='{}' WHERE userid='{}' ".format(cover, userid)))
			conn.commit()
		
		return redirect(url_for('landingPage.dashboard'))
	return redirect(url_for('landingPage.dashboard'))

@dashBoard.route('/tweet', methods=['GET', 'POST'])
def tweet():
	if request.method=='POST':
		userid = session['user']
		time = datetime.datetime.now()

		if 'tweetArea' in request.form:
			post = request.form['tweetArea']
			conn = mysql.connector.connect(host='database-404.cljpc2llv9ft.ap-south-1.rds.amazonaws.com',user='admin', password='admin2114', database='newtwitter')
			cursor = conn.cursor()
			cursor.execute(("INSERT INTO newtwitter_comment (userid, comments, toc) VALUES ('{}','{}','{}')".format(userid,post,time)))
			conn.commit()
			return redirect(url_for('landingPage.dashboard'))


		if 'newTweet' in request.form:
			post = request.form['newTweet']
			conn = mysql.connector.connect(host='database-404.cljpc2llv9ft.ap-south-1.rds.amazonaws.com',user='admin', password='admin2114', database='newtwitter')
			cursor = conn.cursor()
			cursor.execute(("INSERT INTO newtwitter_comment (userid, comments, toc) VALUES ('{}','{}','{}')".format(userid,post,time)))
			conn.commit()
			return redirect(url_for('landingPage.feed'))
	
	return redirect(url_for('landingPage.feed'))
