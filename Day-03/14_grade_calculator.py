marks=int(input("Enter the marks to assign grade:"))
if 90<=marks<=100:
    print("A+")
elif 80<=marks<=89:
    print("A")
elif 70<=marks<=79:
    print("B")
elif 60<=marks<=69:
    print("C")
elif 35<=marks<=59:
    print("D")
else:
    print("Fail")