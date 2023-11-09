from flask import Flask
from flask_login import LoginManager
from flask_minify import Minify
from dotenv import load_dotenv
from .database import db 
from .models import User
from .get_started import init
from .auth import auth
from .root import root
from .member import member
from .books import books
from .borrow import borrow
import os

load_dotenv()

def create_app():
    app = Flask(__name__, template_folder='client', static_folder='static')
    app.config['SECRET_KEY'] = os.urandom(32)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB')

    app.register_blueprint(init, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(root, url_prefix='/')
    app.register_blueprint(member, url_prefix='/member')
    app.register_blueprint(books, url_prefix='/books')
    app.register_blueprint(borrow, url_prefix='/borrow')

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    Minify(app=app, html=True, js=True, cssless=True)
    
    return app