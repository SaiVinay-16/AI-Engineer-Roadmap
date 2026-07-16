li=[1,2,3,4,5]
k=int(input("Enter the k value:"))
k=k%len(li)
while k:
    temp=li[0]
    li.pop(0)
    li.append(temp)
    k-=1
print(li)