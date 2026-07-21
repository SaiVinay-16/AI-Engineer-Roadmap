# student.py

class Student:
    def __init__(self, roll_number, name, cgpa):
        self.roll_number = roll_number
        self.name = name
        self.cgpa = cgpa

    def __str__(self):
        return f"Roll: {self.roll_number}, Name: {self.name}, CGPA: {self.cgpa}"