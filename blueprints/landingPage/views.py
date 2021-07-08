from flask import Blueprint, render_template, session, redirect, url_for, request
import mysql.connector
import dropbox

dropbox_access_token= "xogv50OrMysAAAAAAAAAAZLNZRmAmZXik0U4xaF6EoWmQlFMPiDuw6JmfxzDWTiF"
dropbox_path= "/Apps/newTwitter"
dbx = dropbox.Dropbox(dropbox_access_token)


# conn = mysql.connector.connect(host='freedb.tech',user='freedbtech_rsyst', password='zxcvbnml', database='freedbtech_rsyst')
# cursor = conn.cursor()

landingPage = Blueprint('landingPage',__name__, template_folder='templates', static_folder='static',static_url_path='landingPage/static')

@landingPage.route('/', methods=['POST', 'GET'])
def home():
	if "user" in session:
		return redirect(url_for('.feed'))
	else:
		if request.method=='POST':
			if request.form.get('name', False) and request.form.get('userid', False) and request.form.get('password', False) and request.form.get('month', False) and request.form.get('day', False) and request.form.get('year', False):
				name=request.form['name']
				userid = request.form['userid']
				password = request.form['password']
				month = request.form['month']
				day = request.form['day']
				year= request.form['year']
				#print(type(name), type(phoneNumber), type(password), type(month), type(day), type(year)) #all values are string

				conn = mysql.connector.connect(host='freedb.tech',user='freedbtech_rsyst', password='zxcvbnml', database='freedbtech_rsyst')
				cursor = conn.cursor()
				cursor.execute((" SELECT * FROM newtwitter_user WHERE userid='{}' ".format(userid)))
				user = cursor.fetchall()

				if user:
					return redirect(url_for('.signin'))
				else:
					cursor.execute(("INSERT INTO newtwitter_user (username, userid, password, dob) VALUES ('{}','{}','{}','{}')".format(name, userid,password,year+'-'+month+'-'+day)))
					conn.commit()
					return redirect(url_for('.signin'))

				return render_template('landingPage/newTwitter.html')
		return render_template('landingPage/newTwitter.html')

@landingPage.route('/signin', methods=['POST', 'GET'])
def signin():
	# return render_template('landingPage/signin.html')

	if "user" in session:
		return redirect(url_for('.feed'))
	else:
		if request.method=='POST':
			if request.form.get('userid', False) and request.form.get('password', False):
				userid = request.form['userid']
				password = request.form['password']
				
				conn = mysql.connector.connect(host='freedb.tech',user='freedbtech_rsyst', password='zxcvbnml', database='freedbtech_rsyst')
				cursor = conn.cursor()
				cursor.execute(("SELECT * FROM newtwitter_user WHERE userid='{}'".format(userid)))
				user = cursor.fetchall()

				if user:
					#checking if userid and pass match with those at database
					if user[0][1]==userid and user[0][2]==password:
						#creating session data
						session['user'] = user[0][1]
						return redirect(url_for('.feed'))
					else:
						return render_template('landingPage/signin.html')
				return render_template('landingPage/signin.html')
			return render_template('landingPage/signin.html')
					
		else:
			return render_template('landingPage/signin.html')

@landingPage.route('/dashboard')
def dashboard():
	if "user" in session:
		userid = session['user']
		conn = mysql.connector.connect(host='freedb.tech',user='freedbtech_rsyst', password='zxcvbnml', database='freedbtech_rsyst')
		cursor = conn.cursor()
		cursor.execute(("SELECT * FROM newtwitter_user WHERE userid='{}'".format(userid)))
		user = cursor.fetchall()

		cursor.execute(("SELECT * FROM newtwitter_comment WHERE userid='{}' ORDER BY toc DESC".format(userid)))
		comments = cursor.fetchall()
		try:
			dp = dbx.files_get_temporary_link(f'/{userid}dp.jpg')
			dp =dp.link
			cover = dbx.files_get_temporary_link(f'/{userid}cover.jpg')
			cover = cover.link
			return render_template('dashBoard/profile.html', data=(user,comments, [dp, cover]))
		except:
			return render_template('dashBoard/profile.html', data=(user,comments))

	else:
		return redirect(url_for('.signin'))

@landingPage.route('/home', methods=['GET', 'POST'])
def feed():
	if "user" in session:
		return render_template('dashBoard/homepage.html')

@landingPage.route('/logout', methods=['POST', 'GET'])
def logout():
	session.clear()
	return redirect(url_for('.signin'))
	