num=int(input("Enter the number:"))
for i in range(1,num):
    print(" "*(num-i),end="")
    print("*"*(2*i-1))
for i in range(num,0,-1):
    print(" "*(num-i),end="")
    print("*"*(2*i-1))