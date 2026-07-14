num=int(input("Enter the number:"))
temp=0
dup=num
while dup:
    x=dup%10
    temp1=1
    for i in range(1,x+1):
        temp1*=i
    temp+=temp1
    dup=dup//10
if temp==num:
    print("Strong number")
else:
    print("Not a strong number")