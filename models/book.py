class Book:
    def __init__(self, title, author, genre, checked_out, return_by):
        self.title = title
        self.author = author
        self.genre = genre
        self.checked_out = checked_out
        self.return_by = return_by

    def check_in(self):
        self.checked_out = False
    
    def check_out(self, return_by):
        self.checked_out = True
        self.return_by = return_by