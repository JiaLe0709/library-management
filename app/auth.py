from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from utils.init_function import init_process
from .database import db
from .models import User

auth = Blueprint('auth', __name__, template_folder='client', static_folder='static')

@auth.route('/login', methods=['GET', 'POST'], endpoint='login')
@init_process
def login():
    if current_user.is_authenticated:
        return redirect(url_for('root.home'))
    else:
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
    return render_template('auth/login.html')

@auth.route('/logout', endpoint='logout')
@init_process
@login_required
def logout():
    logout_user()
    flash('Logged Out!', category='success')
    return redirect(url_for('auth.login'))
    
@auth.route('/change-password', endpoint='change_pass', methods=['POST'])
@init_process
@login_required
def change_pass():
    if request.method == 'POST':
        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')

        user = User.query.filter_by(email=current_user.email).first()
        check_pass = check_password_hash(password=current_user.password, pwhash='pbkdf2')
        currc_pass = check_password_hash(password=current_password, pwhash='pbkdf2')
        if check_pass == currc_pass:
            try:
                user.password = generate_password_hash(new_password, method='pbkdf2', salt_length=16)
                db.session.commit()
                flash("You've change the password successfully!", category='success')
                return redirect(url_for('auth.logout'))
            except:
                flash('Failed to change the password!', category='error')
                return redirect(url_for('settings.home'))
        else:
            flash('Incorrect Passwordl!', category='error')
            return redirect(url_for('settings.home'))
    return redirect(url_for('settings.home'))