def palindrome(num):
    temp=len(str(num))-1
    for i in range(len(str(num))//2):
        if str(num)[i]!=str(num)[temp]:
            return "Not a Palindrome"
        temp-=1
    return "Palindrome"
        
num=int(input("Enter the number:"))
st=palindrome(num)
print(st)