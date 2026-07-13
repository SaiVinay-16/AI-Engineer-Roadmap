Name = input("Enter the name:")
for i in Name:
   if i in "aeiouAEIOU":
     Name=Name.replace(i,"")
print(Name)