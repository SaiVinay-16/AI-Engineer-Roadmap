class Student:
    college_name="S.R.K.R"
    def __init__(self,student_name):
        self.student_name=student_name
    @classmethod
    def change(cls):
        cls.college_name="Vishnu"
    def display(self):
        print(f"College : {self.college_name}\nStudent : {self.student_name}")
s1=Student("Saivinay")
s2=Student("Saivivek")
s1.display()
s2.display()
Student.change()
s1.display()
s2.display()