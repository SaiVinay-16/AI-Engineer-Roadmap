def divide(x,y):
    if y==0:
        return "Zero Division error"
    else:
        return x/y
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print(divide(a,b))