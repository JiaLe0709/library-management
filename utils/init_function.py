from flask import redirect, url_for, abort
from app.models import User

def init_process(func):
    def decorated_function(*args, **kwargs):
        if User.query.filter_by(id=1).first() is None:
            return redirect(url_for('init.get_started'))
        return func(*args, **kwargs)
    return decorated_function

def remove_init(func):
    def decorated_function(*args, **kwargs):
        if User.query.filter_by(id=1).first() is not None:
            abort(404)
        return func(*args, **kwargs)
    return decorated_function