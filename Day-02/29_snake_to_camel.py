Name = input("Enter the name:")
temp= Name.split('_')
res=temp[0]
for word in temp[1:]:
    res+=word.capitalize()
print(res)