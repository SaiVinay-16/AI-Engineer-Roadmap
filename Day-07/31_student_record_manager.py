def add_student(filename):
    try:
        with open(filename, "a") as f:  # append mode
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            branch = input("Enter Branch: ")
            cgpa = input("Enter CGPA: ")
            f.write(f"{student_id},{name},{branch},{cgpa}\n")
        print("Student record added successfully.\n")
    except Exception as e:
        print(f"Error while adding student: {e}")


def view_students(filename):
    try:
        with open(filename, "r") as f:
            print("\n--- Student Records ---")
            for line in f:
                student_id, name, branch, cgpa = line.strip().split(",")
                print(f"ID: {student_id}, Name: {name}, Branch: {branch}, CGPA: {cgpa}")
            print("-----------------------\n")
    except FileNotFoundError:
        print("No records found. File does not exist yet.\n")
    except Exception as e:
        print(f"Error while viewing students: {e}")


def search_student(filename):
    try:
        search_id = input("Enter Student ID to search: ")
        found = False
        with open(filename, "r") as f:
            for line in f:
                student_id, name, branch, cgpa = line.strip().split(",")
                if student_id == search_id:
                    print(f"\nStudent Found: ID: {student_id}, Name: {name}, Branch: {branch}, CGPA: {cgpa}\n")
                    found = True
                    break
        if not found:
            print("Student not found.\n")
    except FileNotFoundError:
        print("No records found. File does not exist yet.\n")
    except Exception as e:
        print(f"Error while searching student: {e}")


def menu():
    filename = "students.txt"
    while True:
        print("===== Student Record Manager =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(filename)
        elif choice == "2":
            view_students(filename)
        elif choice == "3":
            search_student(filename)
        elif choice == "4":
            print("Exiting Student Record Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


menu()