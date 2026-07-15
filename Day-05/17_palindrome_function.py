def check_palindrome(num):
    temp=len(str(num))
    x=temp-1
    dup=str(num)
    for i in range(temp//2+1):
        if dup[i] !=dup[x]:
            return "Not a palindrome"
        x-=1
    return "palindrome"
num=int(input("Enter the number:"))
print(check_palindrome(num))