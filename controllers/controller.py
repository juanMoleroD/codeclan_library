from crypt import methods
from datetime import datetime
from flask import render_template, redirect, request
from app import app
from models.book import Book
from models.book_list import books, add_book, checkout_book, remove_book_by_index, checkin_book, remove_book_by_title

@app.route('/books')
def index():
    return render_template('all_books.html', title='CodeClan Library', books=books)

@app.route('/books/<index>')
def book_by_index(index):
    return render_template('book.html', title=books[int(index)].title, book=books[int(index)], book_index=index)

@app.route('/books/new')
def new_book_form():
    return render_template('add_new_book.html', title='New book')

@app.route('/books', methods=['POST'])
def add_new_book():
    #print(request.form)
    new_book = Book(request.form['book-title'], request.form['author'], request.form['genre'], False , datetime.now()) #new books are not yet checked out by default
    add_book(new_book)
    return redirect('/books')

@app.route('/books/delete/<index>')
def delete_book_by_index(index):
    remove_book_by_index(int(index))
    return redirect('/books')

@app.route('/books/check-out', methods=['POST'])
def check_out():
    checkout_book(int(request.form['book-index']), request.form['return-by'])
    redirect_link = '/books/' + request.form['book-index']
    return redirect(redirect_link)

@app.route('/books/check-in/<index>')
def check_in(index):
    checkin_book(int(index))
    redirect_link = '/books/' + index
    return redirect(redirect_link)

@app.route('/books/delete', methods=['POST'])
def delete_by_title():
    remove_book_by_title(request.form['book-title'])
    return redirect('/books')
    