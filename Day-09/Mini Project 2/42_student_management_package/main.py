from student_management import operations, validation

def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                roll = int(input("Enter Roll Number: "))
                name = input("Enter Name: ")
                cgpa = float(input("Enter CGPA: "))

                if not validation.validate_roll_number(roll):
                    print("❌ Invalid Roll Number")
                    continue
                if not validation.validate_cgpa(cgpa):
                    print("❌ Invalid CGPA (0.0 - 10.0)")
                    continue

                operations.add_student(roll, name, cgpa)
            except ValueError:
                print("❌ Invalid input format.")

        elif choice == "2":
            operations.display_students()

        elif choice == "3":
            try:
                roll = int(input("Enter Roll Number to search: "))
                operations.search_student(roll)
            except ValueError:
                print("❌ Invalid input format.")

        elif choice == "4":
            print("👋 Exiting Student Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()