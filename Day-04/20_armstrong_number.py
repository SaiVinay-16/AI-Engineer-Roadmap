num=int(input("Enter the number:"))
dup=num
no_of_dig=len(str(num))
temp=0
while num:
    x=num%10
    temp+=x**no_of_dig
    num=num//10
if dup==temp:
    print("Armgstrong number")
else:
    print("Not an armgstrong number")