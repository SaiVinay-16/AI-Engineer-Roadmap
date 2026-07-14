num=input("Enter the number:")
res=0
power=0
if all(d in '01' for d in num):
    temp=int(num)
    while temp:
        x=temp%10
        res+=x*2**power
        temp=temp//10
        power+=1
else:
    print("Invalid input! Please enter only 0s and 1s.")
print(res)