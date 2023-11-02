from flask import render_template, send_from_directory, redirect, url_for, Blueprint
from flask_login import login_required
from utils.init_function import init_process
import os

root = Blueprint('root', __name__, template_folder='client', static_folder='static')

@root.route('/', endpoint='home')
@init_process
@login_required
def home():
    return render_template('index.html', title='Home', nav=True)

@root.route('/favicon.ico')
def favicon():
  return send_from_directory(os.path.join(root.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@root.errorhandler(401)
def unauthorized(e):
    return redirect(url_for('auth.login'))