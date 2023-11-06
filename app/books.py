from flask import Blueprint, render_template, request, flash
from flask_login import login_required
from utils.currency import currency as cr
from utils.dewey import dewey as dw
from utils.lang import lang as lg
from utils.init_function import init_process
from .models import Books
from .database import db

books = Blueprint("books", __name__, template_folder="client", static_folder="static")

@books.route("/", endpoint="home")
def home():
    return render_template("books/home.html", title="Books")

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
    
    return render_template(
        "books/new.html", title="Books", dewey=dw, currency_=cr, source=source, langs=lg)
