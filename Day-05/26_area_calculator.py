import math

def area_rectangle(length, width):
    return length * width

def area_square(side):
    return side * side

def area_circle(radius):
    return math.pi * (radius ** 2)

def area_triangle(base, height):
    return 0.5 * base * height

def area_calculator():
    print("Choose a shape to calculate area:")
    print("1. Rectangle")
    print("2. Square")
    print("3. Circle")
    print("4. Triangle")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        print("Area of Rectangle:", area_rectangle(length, width))

    elif choice == '2':
        side = float(input("Enter side length: "))
        print("Area of Square:", area_square(side))

    elif choice == '3':
        radius = float(input("Enter radius: "))
        print("Area of Circle:", area_circle(radius))

    elif choice == '4':
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print("Area of Triangle:", area_triangle(base, height))

    else:
        print("Invalid choice!")

area_calculator()