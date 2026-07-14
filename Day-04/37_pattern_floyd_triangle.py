num=int(input("Enter how many rows:"))
temp=1
for i in range(1,num+1):
    for j in range(1,i+1):
        print(temp,end=" ")
        temp+=1
    print("\n")