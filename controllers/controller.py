from flask import render_template, redirect, request
from app import app
from models.book import Book
from models.book_list import books, add_book

@app.route('/books')
def index():
    return render_template('all_books.html', title='CodeClan Library', books=books)

@app.route('/books/<index>')
def book_by_index(index):
    return render_template('book.html', title=books[int(index)].title, book=books[int(index)])

@app.route('/books/new')
def new_book_form():
    return render_template('add_new_book.html', title='New book')

@app.route('/books', methods=['POST'])
def add_new_book():
    print(request.form)
    new_book = Book(request.form['book-title'], request.form['author'], request.form['genre'])
    add_book(new_book)
    return redirect('/books')