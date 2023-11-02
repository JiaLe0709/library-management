from flask import Blueprint, render_template
from flask_login import login_required
from utils.init_function import init_process

member = Blueprint('member', __name__, template_folder='client', static_folder='static')

@member.route('/', endpoint='home')
@init_process
@login_required
def home():
    return render_template('member/home.html', nav=True, title='Member')

@member.route('/new', endpoint='new_member')
@init_process
@login_required
def new_member():
    return render_template('member/new.html', nav=True, title='Create New Member')
