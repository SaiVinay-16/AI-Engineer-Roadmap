def even_or_odd(x):
    if x%2==0:
        return "Even"
    else:
        return "Odd"
a=int(input("Enter the number:"))
print(even_or_odd(a))