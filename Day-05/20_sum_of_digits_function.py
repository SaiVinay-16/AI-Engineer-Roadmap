def sum_of_digits(num):
    res=0
    while num:
        x=num%10
        res+=x
        num=num//10
    print(res)
num=int(input("Enter the Number:"))
sum_of_digits(num)