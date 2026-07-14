num=int(input("Enter the number:"))
temp=0
for i in range(2,num):
    if num%i==0:
        temp=1
        break
if temp==0:
    print("Prime number")
else:
    print("Not a prime number")