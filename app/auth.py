from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from .models import User

auth = Blueprint('auth', __name__, template_folder='client', static_folder='static')

@auth.route('/login', methods=['GET', 'POST'], endpoint='login')
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged In!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('root.home'))
            else:
                flash('Incorrect Password and Email!', category='error')
        else:
            flash('Incorrect Password and Email!', category='error')
    return render_template('auth/login.html', title='Login', nav=True)

@auth.route('/logout', endpoint='logout')
@login_required
def logout():
    logout_user()
    flash('Logged Out!', category='success')
    return redirect(url_for('auth.login'))
