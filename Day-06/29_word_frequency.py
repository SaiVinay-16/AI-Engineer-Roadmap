st="python is easy python is powerful"
temp=st.split()
dici={}
for i in temp:
    if i in dici:
        dici[i]+=1
    else:
        dici[i]=1
print(dici)