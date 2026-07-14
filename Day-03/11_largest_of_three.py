num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
temp=0
for i in num1,num2,num3:
    if i>temp:
        temp=i
print(temp,"is greater among three numbers")