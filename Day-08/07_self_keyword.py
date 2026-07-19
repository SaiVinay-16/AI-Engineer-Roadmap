class Person:
    def __init__(self,name,city):
        self.name=name
        self.city=city
    def display(self):
        print(f"Name : {self.name}\nCity : {self.city}")
p=Person("vinay","cheyyeru")
p.display()