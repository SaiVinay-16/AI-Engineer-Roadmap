class Student:
    college_name="S.R.K.R"
    def __init__(self,student_name):
        self.student_name=student_name
    def display(self):
        print(f"College : {self.college_name}\nStudent : {self.student_name}")
s=Student("Saivinay")
s.display()