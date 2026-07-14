side1=int(input("Enter the first side length:"))
side2=int(input("Enter the second side length:"))
side3=int(input("Enter the third side length:"))
asc=[side1,side2,side3]
asc.sort()
if asc[0]+asc[1]>asc[2]:
    print("It is valid triangle")
else:
    print("It is not a valid triangle")