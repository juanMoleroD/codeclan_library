from datetime import datetime


from datetime import datetime
from models.book import Book

book1 = Book("The Three Musketeers", "Alexandre Dumas", "Novel", True, datetime(2022,7,31).strftime('%Y-%m-%d'))
book2 = Book("Clean Code", "Robert Martin", "Programing", True, datetime(2022,8,6).strftime('%Y-%m-%d'))
book3 = Book("The Alchemist", "Paulo Coelho", "Adventure", False, datetime.now().strftime('%Y-%m-%d'))

books = [book1, book2, book3]

def add_book(new_book):
    books.append(new_book)

def remove_book_by_index(index):
    books.pop(index)

def remove_book_by_title(title):
    book_to_remove = None
    for book in books:
        if book.title == title:
            book_to_remove = book
            break
    if book_to_remove != None:
        books.remove(book_to_remove)
