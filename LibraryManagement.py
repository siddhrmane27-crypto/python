class Book:
    def __init__(self, title): 
        self.title = title
        self.is_issued = False

    def __str__(self): 
        return f"{self.title} - {'Issued' if self.is_issued else 'Available'}"


class Member:
    def __init__(self, name): 
        self.name = name
        self.borrowed = []

    def borrow(self, book, lib):
        if lib.issue(book, self):
            self.borrowed.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} not available")

    def return_book(self, book, lib):
        if book in self.borrowed:
            lib.return_book(book)
            self.borrowed.remove(book)
            print(f"{self.name} returned {book.title}")


class Library:
    def __init__(self):
        self.books = []
        self.issued = {}

    def add(self, book):
        self.books.append(book)

    def issue(self, book, member):
        if book in self.books and not book.is_issued:
            book.is_issued = True
            self.issued[book] = member
            return True
        return False

    def return_book(self, book):
        book.is_issued = False
        self.issued.pop(book, None)

    def show(self):
        print("\nBooks in Library:")
        for b in self.books:
            print(b)
        print("Issued Books:")
        if not self.issued:
            print("None")
        else:
            for b, m in self.issued.items():
                print(f"{b.title} → {m.name}")



lib = Library()
b1, b2 = Book("Python"), Book("DSA")
lib.add(b1)
lib.add(b2)

m1, m2 = Member("Cooper"), Member("Alan")

lib.show()

m1.borrow(b1, lib)
m2.borrow(b1, lib)  
m2.borrow(b2, lib)

lib.show()

m1.return_book(b1, lib)

lib.show()
