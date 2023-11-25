from flask import render_template, redirect, url_for, Blueprint, request, flash
from flask_login import login_required
from utils.init_function import init_process
from .models import Settings
from .database import db
import requests as rq

settings = Blueprint('settings', __name__, template_folder='client', static_folder='static')

@settings.route('/settings', endpoint='home')

def home():
   config = Settings.query.filter_by(id=1).first()
   return render_template('setup/settings.html', config=config)

@settings.route('/config', methods=['POST'], endpoint='config')
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
          return redirect(url_for('settings.home'))
        except:
          flash('Config failed to save !', category='warning') 
          return redirect(url_for('settings.home'))
      else:
        try:
          validate_config_value.deploy_hook=hook
          validate_config_value.fine_price=fined
          db.session.commit()
          flash('Config update Succesfully !', category='success')
          return redirect(url_for('settings.home'))
        except:
          flash('Config failed to update !', category='warning') 
          return redirect(url_for('settings.home')) 
   return redirect(url_for('settings.home'))

@settings.route('/redeploy', methods=['POST'], endpoint='redeploy')
def redeploy():
  return redirect(url_for('settings.home'))