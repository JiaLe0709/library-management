from flask import Blueprint, render_template, request, flash
from utils.auth_function import logged_then_return

auth = Blueprint('auth', __name__, template_folder='client', static_folder='static')

@auth.route('/login', methods=['GET', 'POST'], endpoint='login')
@logged_then_return
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email != 'jle26531@gmail.com' and password != '0709':
            flash('Incorect Password and Username !')
    return render_template('auth/login.html', title='Login', nav=True)
