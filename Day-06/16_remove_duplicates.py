li=[10,20,10,30,20,40]
res=[]
for i in li:
    if i not in res:
        res.append(i)
print(res)