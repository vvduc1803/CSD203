class Book():
    """
    Add a node in linked list
    """
    def __init__(self, bid, title, author, status=0):
        self.bid = bid
        self.title = title
        self.author = author
        self.status = status
        self.next = None

class BorrowBook():
    def __init__(self, bid, borrower):
        """
        Create a node contain bid of book and name of borrower
        :param bid:
        :param borrower:
        """
        self.bid = bid
        self.borrower = borrower
        self.next = None

class Library():
    """
    Is linked list datastructure store information about books
    """
    def __init__(self):
        self.head = None

    def AddBook_(self, bid, title, author):
        """
        Add information of book in to file and return book information
        :param bid: id of book (unique)
        :param title: title of book
        :param author: author of book
        :return: node store information about the book
        """
        # For file

        # For linked list
        book = Book(bid, title, author)
        self.head.next = book

    def __del__(self, remove_bid):
        current_book = self.head
        while current_book.next != None:
            if current_book.next.bid == remove_bid:
                current_book.next = current_book.next.next

            current_book = current_book.next

            break

    def ReturnBook(self, return_bid):
        """
        Use bid return information of this book and set status is available(0)
        :param return_bid:
        :return:
        """
        current_book = self.head
        while current_book != None:
            if current_book.bid == return_bid:
                print(f'Bid: {current_book.bid} - Title: {current_book.title} - Author: {current_book.author}')
                current_book.status = 0
                break
            current_book = current_book.next

        if current_book == None:
            print("Bid doesn't exist")

    def BorrowBook(self):
        borrow_bid = input('Enter book id: ')
        current_book = self.head
        while current_book.next != None:
            if current_book.bid == borrow_bid and current_book.status == 1:
                print('Book was borrowed')
                break
            elif current_book.bid == borrow_bid and current_book.status == 0:
                current_book.status = 1
                return current_book
                break

class BorrowedBook():
    def __init__(self):
        self.head = None
