class Duck:
    def walk(self):
        print("Beck Beck!")
class Person:
    def walk(self):
        print("Hi Hi")
def get_details(object):
    object.walk()
obj1=Duck()
obj2=Person()
get_details(obj1)
get_details(obj2)