class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', price={self.price})"
        
book1 = Book("The Alchemist", "Paulo Coelho", 399)
book2 = Book("Wings of Fire", "A.P.J. Abdul Kalam", 250)

print(book1)
print(book2)