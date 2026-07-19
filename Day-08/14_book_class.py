class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print("Book Details:")
        print(f"Title  : {self.title}")
        print(f"Author : {self.author}")
        print(f"Price  : ₹{self.price}")

book1 = Book("The Alchemist", "Paulo Coelho", 399)
book2 = Book("Wings of Fire", "A.P.J. Abdul Kalam", 250)

book1.display_details()
print("-" * 25)
book2.display_details()