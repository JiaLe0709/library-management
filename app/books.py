from flask import Blueprint, render_template

books = Blueprint('books', __name__, template_folder='client', static_folder='static')

@books.route('/', endpoint='home')
def home():
    return render_template('books/home.html', title='Books')

@books.route('/new', endpoint='new_books')
def new_books():
    return render_template('books/new.html', title='Books')