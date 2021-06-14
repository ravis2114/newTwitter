from flask import Blueprint, render_template

apis = Blueprint('apis',__name__, template_folder='templates')

@apis.route('/apis/')
def index():
	return {'key':'value'}
