class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def __repr__(self):
        return f"Student(Name : {self.name},Age : {self.age},Marks : {self.marks})"
class StudentManager:
    def __init__(self):
        self.students=[]
    def add_student(self,student):
        self.students.append(student)
        print(f"{student.name} added to Students")
    def display_student(self):
        if len(self.students) ==0:
            print("No students are there")
        else:
            for stud in self.students:
                print(f"Name : {stud.name}\nAge : {stud.age}\nMarks : {stud.marks}")
    def search_student(self,name):
        if not self.students:
            print("Not found")
        else:
            for stud in self.students:
                if name.lower() == stud.name.lower():
                    print("Found")
                    return
        print("Not found")
s=StudentManager()

stu1=Student("vinay",21,85)
stu2=Student("Deepak",29,70)
stu3=Student("Sandeep",28,85)

s.add_student(stu1)
s.add_student(stu2)
s.add_student(stu3)
s.display_student()
s.search_student("sandeep")