from . import db
from flask_login import UserMixin
from datetime import datetime, timedelta

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fine_price = db.Column(db.Float(50), unique=True, server_default='1.00')
    deploy_hook = db.Column(db.String(150))

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    gender = db.Column(db.String(150))
    category = db.Column(db.String(150))
    card_number = db.Column(db.String(150), unique=True)
    borrowed_books = db.relationship('BorrowedBook', backref='member', lazy=True)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    author = db.Column(db.String(150))
    isbn = db.Column(db.String(150))
    dewey = db.Column(db.String(150))
    language = db.Column(db.String(150))
    num_pages = db.Column(db.String(150))
    published_year = db.Column(db.String(150))
    publisher = db.Column(db.String(150))
    summary = db.Column(db.String(256))
    barcode = db.Column(db.String(150), unique=True)
    currency = db.Column(db.String(150))
    price = db.Column(db.String(150))
    sources = db.Column(db.String(150))
    sources_info = db.Column(db.String(150))
    borrowed_books = db.relationship('BorrowedBook', backref='book', lazy=True)

class BorrowedBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    books_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    borrow_date = db.Column(db.DateTime, default=datetime.utcnow)

    def default_return_date():
        return datetime.utcnow() + timedelta(days=7)

    return_date = db.Column(db.DateTime, default=default_return_date)