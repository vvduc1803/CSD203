from main import Book

def AddBook(bid, title, author):
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
    return book