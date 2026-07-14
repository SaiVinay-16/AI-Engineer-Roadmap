num=int(input("Enter the number:"))
big=0
while num:
    x=num%10
    if x>big:
        big=x
    num=num//10
print("big number:",big)