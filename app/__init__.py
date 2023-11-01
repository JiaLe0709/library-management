from flask import Flask
from dotenv import load_dotenv
from .database import db 
from .get_started import init
from .auth import auth
from .root import root
import os

load_dotenv()

def create_app():
    app = Flask(__name__, template_folder='client', static_folder='static')
    app.config['SECRET_KEY'] = os.urandom(32)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB')
    app.register_blueprint(init, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(root, url_prefix='/')
    
    db.init_app(app)

    with app.app_context():
        db.create_all()
    
    return app