from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from utils.currency import currency as cr
from utils.dewey import dewey as dw
from utils.lang import lang as lg
from utils.init_function import init_process
from .models import Books
from .database import db

books = Blueprint("books", __name__, template_folder="client", static_folder="static")

@books.route("/", endpoint="home")
@init_process
@login_required
def home():
    books = Books.query.all()
    return render_template("books/home.html", title="Books", books=books, nav=True)

@books.route("/new", endpoint="new_books", methods=["POST", "GET"])
@init_process
@login_required
def new_books():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        isbn = request.form.get("isbn")
        dewey = request.form.get("dewey")
        language = request.form.get("lang")
        num_pages = request.form.get("page")
        published_year = request.form.get("pub_year")
        publisher = request.form.get("pub")
        summary = request.form.get('summary')
        barcode = request.form.get("barcode")
        currency = request.form.get("currency")
        price = request.form.get("price")
        sources = request.form.get("sources")
        sources_info = request.form.get("sources_info")
        
        validate_barcode = Books.query.filter_by(barcode=barcode).first()
        
        if validate_barcode:
            flash('Barcode cannot be duplicated, try again.', category='error')
        else:
            try:
                books = Books(title=title, author=author, isbn=isbn, dewey=dewey, language=language, num_pages=num_pages, published_year=published_year, publisher=publisher, summary=summary, barcode=barcode, currency=currency, price=price, sources=sources, sources_info=sources_info)
                db.session.add(books)
                db.session.commit()
                flash('Books Registered Succesfully !', category='success')
            except:
                flash('Failed to register a new books !', category='error')
        
    source = [{"name": "Donations"}, {"name": "Purchasing"}, {"name": "Other"}]
    
    return render_template("books/new.html", title="Books", dewey=dw, currency_=cr, source=source, langs=lg, nav=True)

@books.route('/delete/<int:books_id>', endpoint='delete_books', methods=['POST'])
@init_process
@login_required
def delete_books(books_id):
    books_to_delete = Books.query.get(books_id)

    if books_to_delete:
        try:
            db.session.delete(books_to_delete)
            db.session.commit()
            flash('Book Record deleted successfully!', category='success')
        except:
            flash('Failed to delete the Book Record !', category='error')
    else:
        flash('Book Record not found!', category='error')

    return redirect(url_for('books.home'))

@books.route('/update/<int:books_id>', endpoint='update_books', methods=['POST', 'GET'])
@init_process
@login_required
def update_books(books_id):
    
    books_to_update = Books.query.get(books_id)

    if not books_to_update:
        flash("Book's Record not found!", category='error')
        return redirect(url_for('books.home'))

    if request.method == 'POST':
        title = request.form.get("title")
        author = request.form.get("author")
        isbn = request.form.get("isbn")
        dewey = request.form.get("dewey")
        language = request.form.get("lang")
        num_pages = request.form.get("page")
        published_year = request.form.get("pub_year")
        publisher = request.form.get("pub")
        summary = request.form.get('summary')
        barcode = request.form.get("barcode")
        currency = request.form.get("currency")
        price = request.form.get("price")
        sources = request.form.get("sources")
        sources_info = request.form.get("sources_info")

        validate_barcode = Books.query.filter_by(barcode=barcode).first()

        if validate_barcode and validate_barcode != books_to_update:
            flash('Barcode Record cannot be duplicated, try again.', category='error')
        else:
            try:
                books_to_update.title = title
                books_to_update.author = author
                books_to_update.isbn = isbn
                books_to_update.dewey = dewey
                books_to_update.language = language
                books_to_update.num_pages = num_pages
                books_to_update.published_year = published_year
                books_to_update.publisher = publisher
                books_to_update.summary = summary
                books_to_update.barcode = barcode
                books_to_update.currency = currency
                books_to_update.price = price
                books_to_update.sources = sources
                books_to_update.sources_info = sources_info

                db.session.commit()
                flash('Books Record updated successfully!', category='success')
            except:
                flash('Failed to update the books record!', category='error')
            return redirect(url_for('books.home'))
        
    source = [{"name": "Donations"}, {"name": "Purchasing"}, {"name": "Other"}]
    return render_template('books/update.html', nav=True, title='Update Books Record', dewey=dw, currency_=cr, source=source, langs=lg, books=books_to_update)