num=int(input("Enter the Number:"))
res=1
while num:
    x=num%10
    res*=x
    num=num//10
print(res)