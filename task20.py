class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        self.books[title] = {"author": author, "available": True}
