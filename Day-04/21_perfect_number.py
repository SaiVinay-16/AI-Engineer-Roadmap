import math
num=int(input("Enter the number:"))
temp_li=0
for i in range(1,int(math.sqrt(num))+1):
    if num%i==0:
        temp_li+=i
        if i != 1 and i != num // i:
            temp_li += num // i
if temp_li==num:
    print("perfect number")
else:
    print("Not a perfect number")