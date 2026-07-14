num=int(input("Enter the number:"))
if num==1:
    print(1,end=" ")
else:
    print(1,end=" ")
    for i in range(3,num+1):
        temp=0
        for j in range(2,i):
            if i%j==0:
                temp=1
                break
        if temp==0:
            print(i,end=" ")