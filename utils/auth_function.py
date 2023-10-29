from flask import session, abort, redirect, url_for
import random
import string

def generate_otp():
    digits = string.digits
    return ''.join(random.choice(digits) for _ in range(6))

def change_password_verify(function):
    def wrapper(*args, **kwargs):
        if "chng_pws" not in session:
            return abort(404)
        else:
            return function(*args, **kwargs)
    return wrapper

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "logged" not in session:
            return abort(401)
        else:
            return function(*args, **kwargs)
    return wrapper

def logged_then_return(function):
    def wrapper(*args, **kwargs):
        if "logged" in session:
          return redirect(url_for('root'))
        else:
            return function()
    return wrapper