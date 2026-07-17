def add_contact():
    try:
        name = input("Enter the name: ")
        phone_number = input("Enter the phone number: ")
        with open("contact_book.txt", "a") as f:
            f.write(f"{name},{phone_number}\n")
        print("=== Added successfully ===\n")
    except Exception as e:
        print(f"Error while adding contact: {e}")


def search_contact():
    try:
        name = input("Enter the name to search: ")
        found = False
        with open("contact_book.txt", "r") as f:
            for line in f:
                contact_name, contact_phone = line.strip().split(",")
                if contact_name.lower() == name.lower():
                    print(f"Contact Found → Name: {contact_name}, Phone: {contact_phone}\n")
                    found = True
                    break
        if not found:
            print("Contact not found.\n")
    except FileNotFoundError:
        print("No contacts available yet.\n")
    except Exception as e:
        print(f"Error while searching contact: {e}")


def display_contacts():
    try:
        with open("contact_book.txt", "r") as f:
            data = f.readlines()
            if data:
                print("\n--- All Contacts ---")
                for line in data:
                    name, phone = line.strip().split(",")
                    print(f"Name: {name}, Phone: {phone}")
                print("--------------------\n")
            else:
                print("There are no contacts available.\n")
    except FileNotFoundError:
        print("No contacts available yet.\n")
    except Exception as e:
        print(f"Error while displaying contacts: {e}")


def main():
    while True:
        print("==============")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice (1/2/3/4): "))
            if choice == 1:
                add_contact()
            elif choice == 2:
                search_contact()
            elif choice == 3:
                display_contacts()
            elif choice == 4:
                print("Exit successful. Goodbye!")
                break
            else:
                print("Choice must be between 1 and 4.\n")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.\n")

main()