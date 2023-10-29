from flask import Flask, render_template, send_from_directory, request, Blueprint
from core.auth import auth
import os

app = Flask(__name__, template_folder='client', static_folder='static')
app.register_blueprint(auth, url_prefix='/')

@app.route('/')
def home():
    return render_template('index.html', title='Home', message='lol', nav=True)

@app.route('/favicon.ico')
def favicon():
  return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)
