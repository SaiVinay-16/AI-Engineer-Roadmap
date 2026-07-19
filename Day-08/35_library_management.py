# =======================IMPORTANT NOTES FOR THIS PROGRAM===========================
# Why doesn't Python call __init__() again?

# This is another important point.

# You said:

# "it goes to book1 object class and in __init__ constructor we already assigned the title"

# Almost correct, but __init__() is not executed again.

# It already ran once, when the object was created.

# Example:

# book1 = Book("The Alchemist", "Paulo Coelho", 399)

# At that moment, Python called:

# Book.__init__(book1, "The Alchemist", "Paulo Coelho", 399)

# and stored:

# title = "The Alchemist"
# author = "Paulo Coelho"
# price = 399

# Later, when you write:

# print(book.title)

# Python simply reads the value that is already stored inside the object.

# It does not call __init__() again.
# ===============================================================================

class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', price={self.price})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(self.books)
        print(f"Book '{book.title}' added to library.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nLibrary Collection:")
            for book in self.books:
                print(f"Title : {book.title}, Author : {book.author}, Price : ₹{book.price}")
            print("-" * 40)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"Book Found → Title: {book.title}, Author: {book.author}, Price: ₹{book.price}")
                return
        print(f"Book '{title}' not found in library.")

library = Library()

book1 = Book("The Alchemist", "Paulo Coelho", 399)
book2 = Book("Wings of Fire", "A.P.J. Abdul Kalam", 250)
book3 = Book("Python Programming", "John Zelle", 550)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()

library.search_book("Wings of Fire")
library.search_book("C++ Basics")