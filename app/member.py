from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from utils.init_function import init_process
from .models import Member
from .database import db

member = Blueprint('member', __name__, template_folder='client', static_folder='static')

@member.route('/', endpoint='home')
@init_process
@login_required
def home():
    member = Member.query.all()
    return render_template('member/home.html', nav=True, title='Member', member=member)

@member.route('/new', endpoint='new_member', methods=['POST', 'GET'])
@init_process
@login_required
def new_member():
    if request.method == 'POST':
        name = request.form.get('name')
        gender = request.form.get('gender')
        category = request.form.get('category')
        ic = request.form.get('ic')

        validate_ic = Member.query.filter_by(card_number=ic).first()
        if validate_ic:
            flash('Ic cannot be duplicated, try again.', category='error')
        else:
            try:
                member = Member(name=name, gender=gender, category=category, card_number=ic)
                db.session.add(member)
                db.session.commit()
                flash('Member Created Succesfully !', category='success')
            except:
                flash('Failed to Create a new member !', category='error')
    return render_template('member/new.html', nav=True, title='Create New Member',
        gender=[{'name':'-'}, {'name':'Female'}, {'name':'Male'}])

@member.route('/delete/<int:member_id>', endpoint='delete_member', methods=['POST'])
@init_process
@login_required
def delete_member(member_id):
    member_to_delete = Member.query.get(member_id)

    if member_to_delete:
        try:
            db.session.delete(member_to_delete)
            db.session.commit()
            flash('Member deleted successfully!', category='success')
        except:
            flash('Failed to delete the member!', category='error')
    else:
        flash('Member not found!', category='error')

    return redirect(url_for('member.home'))