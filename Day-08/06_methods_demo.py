class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print(f"Area of Rectangle : {self.length * self.breadth}")
    def perimeter(self):
        print(f"Perimeter of Rectangle: {2 * (self.length + self.breadth)}")
r=Rectangle(20,20)
r.area()
r.perimeter()