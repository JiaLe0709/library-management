from flask import Blueprint, render_template, request
from utils.auth_function import logged_then_return

auth = Blueprint('auth', __name__, template_folder='client', static_folder='static')

@auth.route('/login', methods=['GET', 'POST'])
@logged_then_return
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
    return render_template('auth/login.html', title='Login', nav=True)
