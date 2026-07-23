num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
res=lambda x,y:x if x>y else y
print(res(num1,num2))