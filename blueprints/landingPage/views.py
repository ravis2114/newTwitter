from flask import Blueprint, render_template, session, redirect, url_for, request
import mysql.connector

conn = mysql.connector.connect(host='freedb.tech',user='freedbtech_rsyst', password='zxcvbnml', database='freedbtech_rsyst')
cursor = conn.cursor()

landingPage = Blueprint('landingPage',__name__, template_folder='templates', static_folder='static',static_url_path='landingPage/static')

@landingPage.route('/', methods=['POST', 'GET'])
def home():
    if "user" in session:
        return redirect(url_for('.dashboard'))
    else:
        if request.method=='POST':
            name=request.form['name']
            userid = request.form['userid']
            password = request.form['password']
            month = request.form['month']
            day = request.form['day']
            year= request.form['year']
            #print(type(name), type(phoneNumber), type(password), type(month), type(day), type(year)) #all values are string

            cursor.execute((" SELECT * FROM newtwitter_user WHERE userid='{}' ".format(userid)))
            user = cursor.fetchall()

            if user:
                return redirect(url_for('.signin'))
            else:
                cursor.execute(("INSERT INTO newtwitter_user (username, userid, userpassword, dob) VALUES ('{}','{}','{}','{}')".format(name, userid,password,day+month+year)))
                conn.commit()
                return redirect(url_for('.signin'))

            return render_template('landingPage/newTwitter.html')
        return render_template('landingPage/newTwitter.html')

@landingPage.route('/signin', methods=['POST', 'GET'])
def signin():
    # return render_template('landingPage/signin.html')

    if "user" in session:
        return redirect(url_for('.dashboard'))
    else:
        if request.method=='POST':
            if request.form['userid'] and request.form['password']:
                userid = request.form['userid']
                password = request.form['password']
                
                cursor.execute(("SELECT * FROM newtwitter_user WHERE userid='{}'".format(userid)))
                user = cursor.fetchall()

                session['user'] = user[0][1]

                if user[0][1]==userid and user[0][2]==password:
                    return render_template('dashBoard/profile.html', data=user)
                else:
                    return render_template('landingPage/signin.html')
                    
        else:
            return render_template('landingPage/signin.html')

@landingPage.route('/dashboard')
def dashboard():
	if "user" in session:
		return render_template('dashBoard/profile.html')
	else:
		return redirect(url_for('.signin'))

@landingPage.route('/logout', methods=['POST', 'GET'])
def logout():
	session.pop('user')
	return redirect(url_for('.signin'))