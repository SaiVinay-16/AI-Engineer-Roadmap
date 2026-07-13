Name = input("Enter the name:")
res=""
for ch in Name:
    if ch not in res:
        res+=ch
print(res)