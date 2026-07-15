def smallest_of_two(x,y):
    if x<y:
        return x
    else:
        return y
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print(smallest_of_two(a,b))