def rev_num(num):
    res=0
    while num:
        x=num%10
        res=res*10+x
        num=num//10
    print(res)
num=int(input("Enter the Number:"))
rev_num(num)