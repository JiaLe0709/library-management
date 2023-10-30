from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from core.auth import auth
from core.root import root
import os

load_dotenv()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='client', static_folder='static')
    app.config['SECRET_KEY'] = os.urandom(32)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(root, url_prefix='/')
    db.init_app(app)

    return app