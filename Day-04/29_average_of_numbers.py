num=int(input("Enter the number:"))
total=0
for i in range(1,num+1):
    print("Enter the ",i," number:")
    temp=int(input())
    total+=temp
avg=total//num
print("Average:",avg)