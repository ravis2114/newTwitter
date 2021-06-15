from flask import Blueprint, render_template, request, redirect, url_for, session
import mysql.connector

main = Blueprint('main',__name__, template_folder='templates', static_folder='static', static_url_path='main/static')


conn = mysql.connector.connect(host='remotemysql.com',user='kEOWWtr4ag', password='dgXWQcifF8', database='kEOWWtr4ag')
cursor = conn.cursor()

@main.route('/signin', methods=['POST', 'GET'])
def signin():
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
				return render_template('main/signin.html')
		else:
			return render_template('main/signin.html')

@main.route('/signup', methods=['POST', 'GET'])
def signup():
	if "user" in session:
		return redirect(url_for('.dashboard'))
	else:
		if request.method=='POST':
			name=request.form['name']
			email=request.form['email']
			password=request.form['password']
			print(name,email,password)

			cursor.execute(("INSERT INTO users (uid,name,email,password) VALUES (NULL, '{}', '{}', '{}')".format(name,email,password)))
			conn.commit()

			return redirect(url_for('.signin'))


		return render_template('main/signup.html')


@main.route('/dashboard')
def dashboard():
	if "user" in session:
		return render_template('main/dashboard.html')
	else:
		return redirect(url_for('.signin'))

@main.route('/logout', methods=['POST', 'GET'])
def logout():
	session.pop('user')
	return redirect(url_for('.signin'))