    Name = input("Enter the name:")
    dici={}
for i in range(len(Name)):
    if Name[i] in dici:
        dici[Name[i]]+=1
    else:
        dici[Name[i]]=1
temp=0
for ch in dici:
    if dici[ch]>temp:
        temp=dici[ch]
print("Most repeated letter is:",temp)