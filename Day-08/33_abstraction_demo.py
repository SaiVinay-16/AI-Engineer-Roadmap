from abc import ABC,abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(f"Area of circle : {math.pi * self.radius **2}")
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print(f"Area of rectangle : {self.length * self.breadth}")
obj1=Circle(20)
obj2=Rectangle(20,20)
obj1.area()
obj2.area()