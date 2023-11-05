from flask import Blueprint, render_template, request
import json

books = Blueprint('books', __name__, template_folder='client', static_folder='static')

@books.route('/', endpoint='home')
def home():
    return render_template('books/home.html', title='Books')

@books.route('/new', endpoint='new_books', methods=['POST', 'GET'])
def new_books():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('title')
        isbn = request.form.get('title')
        dewey = request.form.get('dewey')
        category = request.form.get('title')
        num_pages = request.form.get('title')
        published_year = request.form.get('title')
        publisher = request.form.get('title')
        barcode = request.form.get('title')
        currency = request.form.get('currency')
        price = request.form.get('price')
        sources = request.form.get('sources')
        
    with open('dewey.json') as json_file:
        dewey_file = json.load(json_file)
        
    with open('currency.json') as currency_file:
        currency_data = json.load(currency_file)
        
    source = [
        {
        'name': 'Donations'
        },
        {
        'name': 'Purchasing'
        },
        {
        'name': 'Other'
        }
        ]
    return render_template('books/new.html', title='Books', dewey=dewey_file, currency_=currency_data, source=source)