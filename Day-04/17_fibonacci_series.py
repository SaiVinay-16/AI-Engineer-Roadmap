num=int(input("Enter the number:"))
li=[0,1]
if num==1:
    print(li[0])
elif num==2:
    print(li)
else:
    for i in range(2,num):
        li.append(li[i-1]+li[i-2])
for i in li:
    print(i,end=" ")