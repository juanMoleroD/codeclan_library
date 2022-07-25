from datetime import datetime
import unittest
from models.book import Book

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book1 = Book("The Three Musketeers", "Alexandre Dumas", "Novel", True, datetime(2022,7,22).strftime("%d-%m-%Y"))

    def test_book_has_title(self):
        self.assertEqual("The Three Musketeers", self.book1.title)

    def test_book_has_author(self):
        self.assertEqual("Alexandre Dumas", self.book1.author)
    
    def test_book_has_genre(self):
        self.assertEqual("Novel", self.book1.genre)
    
    def test_book_has_checked_out_marker(self):
        self.assertTrue(self.book1.checked_out)
    
    def test_book_has_return_by_date(self):
        self.assertEqual("22-07-2022", self.book1.return_by)
        
    def test_book_can_be_checked_in(self):
        self.book1.check_in()
        self.assertEqual(False, self.book1.checked_out)
    
    def test_book_can_be_checked_out(self):
        self.book1.check_in()
        self.book1.check_out()
        self.assertEqual(True, self.book1.checked_out)