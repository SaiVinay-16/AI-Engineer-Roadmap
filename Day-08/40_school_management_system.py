class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def display_info(self):
        print(f"Teacher Name : {self.name}, Subject : {self.subject}")


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f"Student Name : {self.name}, Grade : {self.grade}")


class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.teachers = []
        self.students = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        print(self.teachers)
        print(f"Teacher '{teacher.name}' added to {self.school_name}.")

    def add_student(self, student):
        self.students.append(student)
        print(f"Student '{student.name}' added to {self.school_name}.")

    def display_all_info(self):
        print(f"\n--- {self.school_name} Information ---")
        print("\nTeachers:")
        if not self.teachers:
            print("No teachers available.")
        else:
            for teacher in self.teachers:
                teacher.display_info()

        print("\nStudents:")
        if not self.students:
            print("No students enrolled.")
        else:
            for student in self.students:
                student.display_info()
        print("-" * 40)
        
school = School("Sunrise High School")

t1 = Teacher("Mr. Ramesh", "Mathematics")
t2 = Teacher("Ms. Anita", "Science")

s1 = Student("Sai", "10th Grade")
s2 = Student("Priya", "9th Grade")

school.add_teacher(t1)
school.add_teacher(t2)

school.add_student(s1)
school.add_student(s2)

school.display_all_info()