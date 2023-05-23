class BookLibrary:
    """
    Khởi tạo node trong linked list thư viện chứa thông tin về bid, title, author, status(mặc định khả dụng
    khi thêm vào thư viện).
    """
    def __init__(self, bid, title, author, status=0):
        self.bid = bid
        self.title = title
        self.author = author
        self.status = status
        self.next = None

class BorrowerBook:
    """
    Khởi tạo node cho linked list sách cho mượn chứa thông tin về bid và borrower.
    """
    def __init__(self, bid, borrower):
        self.bid = bid
        self.borrower = borrower
        self.next = None

class LinkedList:
    """
    Khởi tạo linked list chung chứa cả thuộc tính của thư viện và danh sách cho mượn.
    """
    def __init__(self):
        self.head = None

    def load_file(self, bid, title, author, status):
        """
        Thêm các sách đã có trong file vào linked list bằng add first cho nhanh.
        """
        new_book = BookLibrary(bid, title, author, status)
        # Thêm sách
        if not self.head:
            self.head = new_book
        else:
            new_book.next = self.head
            self.head = new_book

    def add_book_for_library(self, bid, title, author, status=0):
        """
        Thuộc tính dùng để thêm sách vào thư viện sẽ không khả dụng khi trùng với bid đã tồn tại.

        :return: True nếu thêm sách thành công,
                 [bid, title] nếu trùng bid với sách đã có trong thư viện.
        """
        # Khởi tạo giá trị sách mới
        new_book = BookLibrary(bid, title, author, status)

        # Thêm sách
        if not self.head:
            self.head = new_book
            return True
        else:
            current = self.head

            # Chạy qua linked list
            while current.next:

                # Trùng id
                if current.bid == bid:
                    return [bid, title]

                current = current.next
            if current.bid == bid:
                return [bid, title]
            else:
                current.next = new_book
                return True

    def add_book_for_borrower(self, bid, borrower):
        """
        Thuộc tính thêm sách vào danh sách cho mượn.
        """
        new_book = BorrowerBook(bid, borrower)
        if not self.head:
            self.head = new_book
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_book

    def remove_book(self, bid):
        """
        Xóa sách khởi thư viện.
        :return: True nếu xóa thành công
                 False nếu sách không tồn tại
        """
        current = self.head
        previous = None
        while current:
            if current.bid == bid:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False

    def display_books(self):
        """
        Hiển thị thông tin sách hiện có trong thư viện.
        """
        current = self.head
        if not current:
            print("No books found.")
            return
        header = " {:<5} | {:<15} | {:<25} | {:<6} ".format("Bid", "Title", "Author", "status")
        print(header)
        print("-"*len(header))
        while current:
            print(" {:<5} | {:<15} | {:<25} | {:<6} ".format(current.bid, current.title, current.author, current.status))
            current = current.next

class Library:
    def __init__(self):
        self.books = LinkedList()
        self.borrowed_books = LinkedList()

        # Thêm các sách có sẵn trong file vào books nếu có
        with open('library_info.txt', 'r') as file:
            file = file.readlines()[1:]
            file = [ele.split('|') for ele in file]
            file.reverse()
            for bid, title, author, status in file:
                self.load_element(bid, title, author, status[0])

    def load_element(self, bid, title, author, status):
        self.books.load_file(bid, title, author, status)

    def add_book(self, bid, title, author, status=0):
        result = self.books.add_book_for_library(bid, title, author, status)
        return result

    def remove_book(self, bid):
        if not self.books.remove_book(bid):
            print(f"No book found with id: {bid}")

    def display_books(self):
        self.books.display_books()

    def borrow_book(self, bid, borrower):
        """
        Thêm thông tin bid, borrower vào danh sách cho mượn và status từ 0 sang
        """
        current = self.books.head
        while current:
            if current.bid == bid:
                if current.status == 0:
                    current.status = 1
                    self.borrowed_books.add_book_for_borrower(bid, borrower)
                    print(f"{current.title} has been borrowed by {borrower}.")
                else:
                    print(f"{current.title} is not available for borrowing.")
                return
            current = current.next
        print(f"No book found with id: {bid}")

    def return_book(self, bid):
        """
        Xóa sách từ danh sách cho mượn và chuyển status từ 1 sang 0
        """
        current = self.books.head
        while current:
            if current.bid == bid:
                current.status = 0
                self.borrowed_books.remove_book(bid)
                print(f"{current.title} has been returned.")
                return
            current = current.next
        print(f"No borrowed book found with id: {bid}")

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Delete Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit\n")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            bid = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            result = library.add_book(bid, title, author)
            while result is not True:
                print(f"Exist book with bid {result[0]}, can't add book {result[1]} to library.")
                bid = input("Enter other book ID: ")
                result = library.add_book(bid, title, author)

            print(f"Book {title} has been added to the library.")

        elif choice == "2":
            print("\nList of books in the library:")
            library.display_books()

        elif choice == "3":
            bid = input("Enter book ID: ")
            library.remove_book(bid)

        elif choice == "4":
            bid = input("Enter book ID to borrow: ")
            borrower = input("Enter borrower name: ")
            library.borrow_book(bid, borrower)

        elif choice == "5":
            bid = input("Enter book ID to return: ")
            library.return_book(bid)

        elif choice == "6":
            print("\nThank you for using the Library Management System.")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
