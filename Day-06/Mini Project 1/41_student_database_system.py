students = []

def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll Number: ")
    branch = input("Enter Branch: ")
    cgpa = float(input("Enter CGPA: "))
    student = {"Name": name, "Roll": roll, "Branch": branch, "CGPA": cgpa}
    students.append(student)
    print("Student added successfully!")

def search_student():
    roll = input("Enter Roll Number to search: ")
    for student in students:
        if student["Roll"] == roll:
            print("\n--- Student Found ---")
            for key, value in student.items():
                print(f"{key}: {value}")
            return
    print("Student not found!")

def update_student():
    roll = input("Enter Roll Number to update: ")
    for student in students:
        if student["Roll"] == roll:
            print("Enter new details (leave blank to keep old value):")
            name = input(f"Name ({student['Name']}): ") or student["Name"]
            branch = input(f"Branch ({student['Branch']}): ") or student["Branch"]
            cgpa_input = input(f"CGPA ({student['CGPA']}): ")
            cgpa = float(cgpa_input) if cgpa_input else student["CGPA"]

            student["Name"] = name
            student["Branch"] = branch
            student["CGPA"] = cgpa
            print("Student updated successfully!")
            return
    print("Student not found!")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    for student in students:
        if student["Roll"] == roll:
            students.remove(student)
            print("Student deleted successfully!")
            return
    print("Student not found!")

def display_students():
    if not students:
        print("No students in database!")
    else:
        print("\n--- All Students ---")
        for student in students:
            for key, value in student.items():
                print(f"{key}: {value}")
            print("---------------------------")

while True:
    print("\n--- Student Database Menu ---")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        add_student()
    elif choice == 2:
        search_student()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        display_students()
    elif choice == 6:
        print("Exiting Student Database System... Goodbye!")
        break
    else:
        print("Invalid choice! Please enter between 1-6.")