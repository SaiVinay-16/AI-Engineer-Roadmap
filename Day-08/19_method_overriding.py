class Vehicle:
    def start(self):
        print("It is the vehicle class")
class Bike(Vehicle):
    def start(self):
        print("It is bike class")
b=Bike()
b.start()