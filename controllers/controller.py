from flask import render_template, redirect, request
from app import app
from models.book_list import books

@app.route('/books')
def index():
    return render_template('all_books.html', title='CodeClan Library', books=books)
