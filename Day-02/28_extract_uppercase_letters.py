Name = input("Enter the uname:")
res=""
for i in Name:
    if i.isupper():
        res+=i
print(res)