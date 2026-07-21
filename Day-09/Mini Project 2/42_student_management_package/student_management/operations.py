# operations.py
from student_management.student import Student

students = []

def add_student(roll_number, name, cgpa):
    student = Student(roll_number, name, cgpa)
    students.append(student)
    print("✅ Student added successfully!")

def display_students():
    if not students:
        print("No students found.")
    else:
        for s in students:
            print(s)

def search_student(roll_number):
    for s in students:
        if s.roll_number == roll_number:
            print("🎯 Student found:", s)
            return
    print("❌ Student not found.")
