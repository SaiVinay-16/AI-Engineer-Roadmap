num=int(input("Enter the number:"))
even_digits=0
odd_digits=0
while num:
    x=num%10
    if x%2==0:
        even_digits+=1
    else:
        odd_digits+=1
    num=num//10
print("Even digits:",even_digits)
print("Odd digits:",odd_digits)