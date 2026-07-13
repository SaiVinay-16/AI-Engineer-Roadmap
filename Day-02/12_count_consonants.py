Name = input("Enter the name:")
res=0
for i in Name:
   if i not in "aeiouAEIOU":
       res+=1
print("The number of consonants in Name is :",res)