import unittest
from models.book import Book

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book1 = Book("The Three Musketeers", "Alexandre Dumas", "Novel")

    def test_book_has_title(self):
        self.assertEqual("The Three Musketeers", self.book1.title)

    def test_book_has_author(self):
        self.assertEqual("Alexandre Dumas", self.book1.author)
    
    def test_book_has_genre(self):
        self.assertEqual("Novel", self.book1.genre)