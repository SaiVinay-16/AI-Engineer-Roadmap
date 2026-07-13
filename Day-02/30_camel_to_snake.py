Name = input("Enter the name:")
res=""
for ch in Name:
    if ch.isupper():
        res=res+"_"+ch.lower()
    else:
        res+=ch
print(res)