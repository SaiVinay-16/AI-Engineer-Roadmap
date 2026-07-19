class Animal:
    @classmethod
    def parent(self):
        print("Below are animals")
class Dog(Animal):
    def sound(self):
        print("Bow Bow")
class Cat(Animal):
    def sound(self):
        print("Meow Meow")
obj1=Dog()
obj2=Cat()
Animal.parent()
obj1.sound()
obj2.sound()