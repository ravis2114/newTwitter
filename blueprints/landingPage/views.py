from flask import Blueprint, render_template, session, redirect, url_for, request
import mysql.connector

conn = mysql.connector.connect(host='remotemysql.com',user='kEOWWtr4ag', password='dgXWQcifF8', database='kEOWWtr4ag')
cursor = conn.cursor()

landingPage = Blueprint('landingPage',__name__, template_folder='templates', static_folder='static',static_url_path='landingPage/static')

@landingPage.route('/', methods=['POST', 'GET'])
def home():
    return render_template('landingPage/newTwitter.html')

@landingPage.route('/signin', methods=['POST', 'GET'])
def signin():
    # return render_template('landingPage/signin.html')

    if "user" in session:
        return redirect(url_for('.dashboard'))
    else:
        if request.method=='POST':
            if request.form['email'] and request.form['password']:
                email = request.form['email']
                password = request.form['password']
                
                cursor.execute(("SELECT * FROM users WHERE email LIKE '{}'".format(email)))
                users = cursor.fetchall()

                session['user'] = users[0][1]

                if len(users)>0:
                    return redirect(url_for('.dashboard'))
                else:
                    return render_template('landingPage/signin.html')
                    
        else:
            return render_template('landingPage/signin.html')

@landingPage.route('/dashboard')
def dashboard():
	if "user" in session:
		return render_template('landingPage/dashboard.html')
	else:
		return redirect(url_for('.signin'))

@landingPage.route('/logout', methods=['POST', 'GET'])
def logout():
	session.pop('user')
	return redirect(url_for('.signin'))