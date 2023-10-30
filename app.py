from flask import Flask, render_template, send_from_directory, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from core.auth import auth
from utils.auth_function import login_is_required
import os

db = SQLAlchemy()
DB_NAME = "database.db"

app = Flask(__name__, template_folder='client', static_folder='static')
app.config['SECRET_KEY'] = os.urandom(32)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.register_blueprint(auth, url_prefix='/')
db.init_app(app)

@app.route('/',  endpoint='home')
@login_is_required
def home():
    return render_template('index.html', title='Home', nav=True)

@app.route('/favicon.ico')
def favicon():
  return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.errorhandler(401)
def unauthorized(e):
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)
