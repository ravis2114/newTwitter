import os
from flask import Flask, render_template

from blueprints.main.views import main
from blueprints.api.views import apis

def create_app():
	app = Flask(__name__)

	app.secret_key = "fuvdlbbdkjbv8734r93-kcjkfdbvk@#$F%$" #os.environ.get('SECRET_KEY')
	#app.config.from_object([os.environ['APP_SETTINGS']])

	app.register_blueprint(main, url_prefix='/home')
	app.register_blueprint(apis)

	@app.route('/')
	def newTwitter():
		return render_template('newTwitter.html')


	return app


if __name__=="__main__":
	create_app().run(host="127.0.0.1", port=5000, debug=True)