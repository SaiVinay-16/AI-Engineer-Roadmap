library = []

def add_book():
    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    book = {"Name": name, "Author": author, "Available": True}
    library.append(book)
    print("Book added successfully!")

def search_book():
    name = input("Enter Book Name to search: ")
    for book in library:
        if book["Name"].lower() == name.lower():
            print("\n--- Book Found ---")
            for key, value in book.items():
                print(f"{key}: {value}")
            return
    print("Book not found!")

def issue_book():
    name = input("Enter Book Name to issue: ")
    for book in library:
        if book["Name"].lower() == name.lower():
            if book["Available"]:
                book["Available"] = False
                print("Book issued successfully!")
            else:
                print("Book is already issued!")
            return
    print("Book not found!")

def return_book():
    name = input("Enter Book Name to return: ")
    for book in library:
        if book["Name"].lower() == name.lower():
            if not book["Available"]:
                book["Available"] = True
                print("Book returned successfully!")
            else:
                print("Book was not issued!")
            return
    print("Book not found!")

def remove_book():
    name = input("Enter Book Name to remove: ")
    for book in library:
        if book["Name"].lower() == name.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found!")

def display_books():
    if not library:
        print("No books in library!")
    else:
        print("\n--- Library Books ---")
        for book in library:
            for key, value in book.items():
                print(f"{key}: {value}")
            print("---------------------------")

while True:
    print("\n--- Library Management Menu ---")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Remove Book")
    print("6. Display All Books")
    print("7. Exit")

    choice = int(input("Enter your choice (1-7): "))

    if choice == 1:
        add_book()
    elif choice == 2:
        search_book()
    elif choice == 3:
        issue_book()
    elif choice == 4:
        return_book()
    elif choice == 5:
        remove_book()
    elif choice == 6:
        display_books()
    elif choice == 7:
        print("Exiting Library Management System... Goodbye!")
        break
    else:
        print("Invalid choice! Please enter between 1-7.")