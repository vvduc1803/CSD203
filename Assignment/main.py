from AddBook import AddBook
from DeleteBook import DeleteBook


class Book():
    def __init__(self, bid, title, author, status=0):
        self.bid = bid
        self.title = title
        self.author = author
        self.status = status
        self.next = None
class Library():
    def __init__(self):
        self.head = None

    def AddBook_(self, bid, title, author):
        book = AddBook(bid, title, author)
        self.head.next = book

    def
