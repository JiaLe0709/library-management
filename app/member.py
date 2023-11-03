from flask import Blueprint, render_template, request
from flask_login import login_required
from utils.init_function import init_process
from .models import Member

member = Blueprint('member', __name__, template_folder='client', static_folder='static')

@member.route('/', endpoint='home')
@init_process
@login_required
def home():
    return render_template('member/home.html', nav=True, title='Member')

@member.route('/new', endpoint='new_member', methods=['POST', 'GET'])
@init_process
@login_required
def new_member():
    if request.method == 'POST':
        name = request.form.get('name')
        gender = request.form.get('gender')
        category = request.form.get('category')
        ic = request.form.get('ic')

        print(name, gender, category, ic)
    return render_template('member/new.html', nav=True, title='Create New Member',
        gender=[{'name':'-'}, {'name':'Female'}, {'name':'Male'}])
