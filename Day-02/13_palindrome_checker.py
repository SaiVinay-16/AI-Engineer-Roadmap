Name = input("Enter the name:")
temp=len(Name)-1
res=True
for i in range(len(Name)//2):
    if Name[i] != Name[temp]:
        res=False
        break
    temp-=1
if res==True:
    print("The given string is Palindrome")
else:
    print("The given string is Not a Palindrome")