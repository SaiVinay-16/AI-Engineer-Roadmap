st="programming"
dici={}
for i in st:
    if i in dici:
        dici[i]+=1
    else:
        dici[i]=1
for key,value in dici.items():
    print(f"{key} : {value}")