from flask import Blueprint, render_template

landingPage = Blueprint('main',__name__, template_folder='templates', static_folder='static')

@landingPage.route('/', methods=['POST', 'GET'])
def home():
    return render_template('newTwitter.html')