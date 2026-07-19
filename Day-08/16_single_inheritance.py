class Person:
    def __init__(self):
        self.name="Saivinay"
class Student(Person):
    def get_details(self):
        print(f"My name is {self.name}")
obj=Child()
obj.get_details()