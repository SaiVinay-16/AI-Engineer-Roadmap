class Person:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class Student(Person):
    def __init__(self,a,b,c,d):
        super().__init__(a,b)
        self.c=c
        self.d=d
    def get_details(self):
        print(f"A : {self.a}\nB : {self.b}\nC : {self.c}\nD : {self.d}")
obj=Student(1,2,3,4)
obj.get_details()