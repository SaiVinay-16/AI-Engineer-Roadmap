# Contact Management System using Dictionary
contacts = {}

while True:
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        contacts[name] = number
        print("Contact added successfully!")

    elif choice == 2:
        name = input("Enter name to update: ")
        if name in contacts:
            number = input("Enter new number: ")
            contacts[name] = number
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    elif choice == 3:
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == 4:
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"{name} : {contacts[name]}")
        else:
            print("Contact not found!")

    elif choice == 5:
        if contacts:
            print("\n--- All Contacts ---")
            for name, number in contacts.items():
                print(f"{name} : {number}")
        else:
            print("No contacts available!")

    elif choice == 6:
        print("Exiting Contact Management System... Goodbye!")
        break

    else:
        print("Invalid choice! Please enter between 1-6.")