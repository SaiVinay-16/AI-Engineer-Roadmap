dici={"name":"Sai vinay","Age":21,"branch":"Artificial Intillegence and data science","college":"S.R.K.R"}
for key,value in dici.items():
    print(f"{key} : {value}")
dici["Age"]=30
print("After updation:")
for key,value in dici.items():
    print(f"{key} : {value}")