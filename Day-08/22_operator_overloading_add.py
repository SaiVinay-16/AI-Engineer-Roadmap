class Student:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self,other):
        res=self.marks+other.marks
        print(res)
s1=Student(20)
s2=Student(20)
s1+s2