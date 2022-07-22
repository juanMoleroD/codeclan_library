from models.book import Book

book1 = Book("The Three Musketeers", "Alexandre Dumas", "Novel")
book2 = Book("Clean Code", "Robert Martin", "Programing")
book3 = Book("The Alchemist", "Paulo Cohelo", "Adventure")

books = [book1, book2, book3]

def add_book(new_book):
    books.append(new_book)