def check_prime(num):
    temp=0
    for i in range(2,num):
        if num%i==0:
            temp=1
            break
    if temp==0:
        return "Prime number"
    else:
        return "Not a prime number"

num=int(input("Enter the number:"))
print(check_prime(num))