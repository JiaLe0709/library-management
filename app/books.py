from flask import Blueprint, render_template, request
from utils.currency import currency as cr
from utils.dewey import dewey as dw
from utils.lang import lang as lg

books = Blueprint("books", __name__, template_folder="client", static_folder="static")

@books.route("/", endpoint="home")
def home():
    return render_template("books/home.html", title="Books")

@books.route("/new", endpoint="new_books", methods=["POST", "GET"])
def new_books():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("title")
        isbn = request.form.get("title")
        dewey = request.form.get("dewey")
        language = request.form.get("lang")
        num_pages = request.form.get("page")
        published_year = request.form.get("pub_year")
        publisher = request.form.get("pub")
        barcode = request.form.get("barcode")
        currency = request.form.get("currency")
        price = request.form.get("price")
        sources = request.form.get("sources")
        sources_info = request.form.get("sources_info")
        
    source = [{"name": "Donations"}, {"name": "Purchasing"}, {"name": "Other"}]
    
    return render_template(
        "books/new.html", title="Books", dewey=dw, currency_=cr, source=source, langs=lg)
