from flask import render_template, send_from_directory, redirect, url_for, Blueprint, request, flash
from flask_login import login_required
from utils.init_function import init_process
from .models import Settings
from .database import db
import os

root = Blueprint('root', __name__, template_folder='client', static_folder='static')

@root.route('/', endpoint='home')
@init_process
@login_required
def home():
    return render_template('index.html')

@root.route('/settings', endpoint='settings')
@init_process
@login_required
def settings():
   config = Settings.query.filter_by(id=1).first()
   return render_template('setup/settings.html', config=config)

@root.route('/config', methods=['POST'])
@init_process
@login_required
def config():
   if request.method == 'POST':
      hook = request.form.get('hook')
      fined = request.form.get('fined')
      validate_config_value = Settings.query.filter_by(id=1).first()
      if not validate_config_value:
        try:
          values = Settings(deploy_hook=hook, fine_price=fined)
          db.session.add(values)
          db.session.commit()
          flash('Config saved Succesfully !', category='success')
          return redirect(url_for('root.settings'))
        except:
          flash('Config failed to save !', category='warning') 
          return redirect(url_for('root.settings'))
      else:
        try:
          validate_config_value.deploy_hook=hook
          validate_config_value.fine_price=fined
          db.session.commit()
          flash('Config update Succesfully !', category='success')
          return redirect(url_for('root.settings'))
        except:
          flash('Config failed to update !', category='warning') 
          return redirect(url_for('root.settings')) 
   return redirect(url_for('root.settings'))

@root.route('/favicon.ico')
def favicon():
  return send_from_directory(os.path.join(root.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@root.errorhandler(401)
def unauthorized(e):
    return redirect(url_for('auth.login'))