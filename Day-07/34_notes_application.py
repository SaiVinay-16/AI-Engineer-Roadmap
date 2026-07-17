def add_note(filename):
    try:
        note = input("Enter your note: ")
        with open(filename, "a") as f:
            f.write(note + "\n")
        print("=== Note Added Successfully ===\n")
    except Exception as e:
        print(f"Error while adding note: {e}\n")


def view_notes(filename):
    try:
        with open(filename, "r") as f:
            notes = f.readlines()
            if notes:
                print("\n--- All Notes ---")
                for i, note in enumerate(notes, start=1):
                    print(f"{i}. {note.strip()}")
                print("-----------------\n")
            else:
                print("No notes available.\n")
    except FileNotFoundError:
        print("No notes file found yet.\n")
    except Exception as e:
        print(f"Error while viewing notes: {e}\n")


def delete_all_notes(filename):
    try:
        with open(filename, "w") as f:
            pass  # overwrite with empty content
        print("=== All Notes Deleted Successfully ===\n")
    except Exception as e:
        print(f"Error while deleting notes: {e}\n")


def main():
    filename = "notes.txt"
    while True:
        print("============== Notes Application ==============")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete All Notes")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice (1/2/3/4): "))
            if choice == 1:
                add_note(filename)
            elif choice == 2:
                view_notes(filename)
            elif choice == 3:
                delete_all_notes(filename)
            elif choice == 4:
                print("Exiting Notes Application. Goodbye!")
                break
            else:
                print("Choice must be between 1 and 4.\n")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.\n")


main()