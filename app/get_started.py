from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash
from utils.init_function import remove_init
from .models import User
from . import db

init = Blueprint('init', __name__, template_folder='client', static_folder='static')

@init.route('/get-started', endpoint='get_started', methods=['POST', 'GET'])
@remove_init
def get_started():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('name')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if password2 != password:
            flash('The password is not match.', category='error')
        else:
            final_password = password
            try:
                new_user = User(email=email, username=username ,password=generate_password_hash(final_password, method='pbkdf2', salt_length=16))
                db.session.add(new_user)
                db.session.commit()
                flash('Account Created Successfully !', category='success')
                return redirect(url_for('root.home'))
            except:
                flash('Failed to Create an account !', category='error')
    return render_template('installation/get-started.html', title='Get Started', nav=True)