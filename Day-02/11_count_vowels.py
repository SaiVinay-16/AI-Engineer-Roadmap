Name = input("Enter the name:")
res=0
for i in Name:
   if i in "aeiouAEIOU":
       res+=1
print("The number of vowels in Name is :",res)