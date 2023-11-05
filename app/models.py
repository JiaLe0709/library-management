from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    gender = db.Column(db.String(150))
    category = db.Column(db.String(150))
    card_number = db.Column(db.String(150), unique=True)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    author = db.Column(db.String(150))
    isbn = db.Column(db.String(150))
    dewey = db.Column(db.String(150))
    language = db.Column(db.String(150))
    num_pages = db.Column(db.Float(50))
    published_year = db.Column(db.Integer)
    publisher = db.Column(db.String(150))
    barcode = db.Column(db.String(150), unique=True)
    currency = db.Column(db.String(150))
    price = db.Column(db.Float(50))
    sources = db.Column(db.String(150))
    sources_info = db.Column(db.String(150))
    