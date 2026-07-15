def check_armstrong(num):
     dup=num
     no_of_dig=len(str(num))
     temp=0
     while num:
         x=num%10
         temp+=x**no_of_dig
         num=num//10
     if dup==temp:
         return "Armgstrong number"
     else:
         return "Not an armgstrong number"

num=int(input("Enter the number:"))
print(check_armstrong(num))