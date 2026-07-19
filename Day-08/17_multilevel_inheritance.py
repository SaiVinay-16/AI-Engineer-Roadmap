class Person:
    def display1(self):
        print("Grand Parent class")
class Student(Person):
    def display2(self):
        print("Child class")
class CollegeStudent(Student):
    def display3(self):
        print("Grand child class")
obj=CollegeStudent()
obj.display1()
obj.display2()
obj.display3()