from blueprints.landingPage.views import dashboard
from flask import Blueprint, render_template, session, redirect, url_for, request

dashBoard = Blueprint('dashBoard',__name__, template_folder='templates', static_folder='static',static_url_path='dashBoard/static')

@dashBoard.route('/', methods=['POST', 'GET'])
def home():
    return render_template('dashBoard/profile.html')
