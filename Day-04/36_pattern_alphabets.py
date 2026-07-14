num=int(input("Enter how many rows:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print("\n")