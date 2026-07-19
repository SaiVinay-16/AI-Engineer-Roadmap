class Parent:
    def __init__(self):
        print("Hi i am Parent class")
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Hi i am Child class")
obj=Child()