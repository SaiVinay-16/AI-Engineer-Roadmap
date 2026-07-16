st="python is easy python is powerful"
temp_li=st.split()
res=[]
for i in temp_li:
    if i not in res:
        res.append(i)
for i in res:
    print(i,end=" ")