num=int(input("Enter the number:"))
dup=num
binary=""
while dup>0:
    binary=str(dup%2)+binary
    dup=dup//2
print(binary)