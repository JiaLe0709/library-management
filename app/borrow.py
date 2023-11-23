from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required
from utils.init_function import init_process
from .models import Member, Books, BorrowedBook
from utils.fine import calculate_fine
from .database import db
from datetime import datetime

borrow = Blueprint('borrow', __name__, template_folder="client", static_folder="static")

@borrow.route('/', methods=['POST', 'GET'], endpoint='home')
@init_process
@login_required
def borrow_book():
    if request.method == "POST":
        n_c = request.form.get('brc')
        member = Member.query.filter_by(card_number=n_c).first()
        
        if member:
            return redirect(url_for('borrow.borrow_books', member_id = member.id))
        
        else:
            flash("Memeber Not Found, Try again !", category='error')
        #book = Books.query.get(book_id)

    """if member.can_borrow_book():
        borrowed_book = BorrowedBook(member=member, book=book)
        db.session.add(borrowed_book)
        db.session.commit()
        flash(f'You have successfully borrowed {book.title}')
    else:
        flash(f'You have reached the maximum number of borrowed books.')"""

    return render_template('borrow/borrow.html', nav=True, title='Borrow Books')

@borrow.route('/<int:member_id>', endpoint='borrow_books', methods=['POST', 'GET'])
@init_process
@login_required
def borrow_books(member_id):
    member = Member.query.get(member_id)
    current_datetime = datetime.utcnow()
    print(int(current_datetime.strftime('%d')))
    if not member:
        flash("Member not found.", category='error')
        return redirect(url_for('borrow.home'))

    books = BorrowedBook.query.filter_by(member_id=member_id).all()
    
    fine_list = [int(current_datetime.strftime('%d')) - int(b.return_date.strftime('%d')) for b in books]
    for i, b in enumerate(books):
        b.fine = fine_list[i]


    if request.method == 'POST':
        if len(books) >= 2:
            flash("You have reached the maximum number of borrowed books (2 books per member).", category='error')
        else:
            
            books_barcode = request.form.get('books')
            validate_barcode = Books.query.filter_by(barcode=books_barcode).first()
            if validate_barcode:
                # Check if the book is already borrowed
                if BorrowedBook.query.filter_by(books_id=validate_barcode.id).first():
                    flash("This book is already borrowed by another member.", category='error')
                else:
                    try:
                        borrow_books = BorrowedBook(books_id=int(validate_barcode.id), member_id=int(member.id))
                        db.session.add(borrow_books)
                        db.session.commit()
                        flash("You've successfully borrowed this book!", category='success')
                        return redirect(url_for('borrow.borrow_books', member_id=member.id))
                    except:
                        flash('Failed to borrow the book!', category='error')
            else:
                flash("Books Barcode Not Found!", category='error')

    return render_template('borrow/borrows.html', nav=True, title='Borrow Books', member=member, books=books, fine=fine_list, datetime=current_datetime)

@borrow.route('/return_book/<int:borrowed_book_id>',endpoint='return_book' ,methods=['POST'])
@init_process
@login_required
def return_book(borrowed_book_id):
    borrowed_book = BorrowedBook.query.get(borrowed_book_id)

    if borrowed_book:
        db.session.delete(borrowed_book)
        db.session.commit()

        flash("You've successfully returned the book!", category='success')
    else:
        flash("Borrowed book not found.", category='error')

    return redirect(url_for('borrow.borrow_books', member_id=borrowed_book.member_id))

