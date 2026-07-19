class Dog:
    def sound(self):
        print("Bow Bow!")
class Cat:
    def sound(self):
        print("Meow Meow!")
class Cow:
    def sound(self):
        print("Ambaa Ambaa!")
def get_details(object):
    object.sound()
obj1=Dog()
obj2=Cat()
obj3=Cow()
get_details(obj1)
get_details(obj2)
get_details(obj3)