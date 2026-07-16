# Menu-driven dictionary program
phonebook = {}

while True:
    print("\n--- Dictionary Menu ---")
    print("1. Add")
    print("2. Update")
    print("3. Delete")
    print("4. Search")
    print("5. Display")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        name = input("Enter name: ")
        number = input("Enter number: ")
        phonebook[name] = number
        print("Contact added successfully!")

    elif choice == 2:
        name = input("Enter name to update: ")
        if name in phonebook:
            number = input("Enter new number: ")
            phonebook[name] = number
            print("Contact updated successfully!")
        else:
            print("Name not found!")

    elif choice == 3:
        name = input("Enter name to delete: ")
        if name in phonebook:
            del phonebook[name]
            print("Contact deleted successfully!")
        else:
            print("Name not found!")

    elif choice == 4:
        name = input("Enter name to search: ")
        if name in phonebook:
            print(f"{name} : {phonebook[name]}")
        else:
            print("Name not found!")

    elif choice == 5:
        if phonebook:
            print("\n--- All Contacts ---")
            for name, number in phonebook.items():
                print(f"{name} : {number}")
        else:
            print("Phonebook is empty!")

    elif choice == 6:
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice! Please enter between 1-6.")