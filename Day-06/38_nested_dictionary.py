dici={"student 1":{"name":"Saivinay","branch" : "AI&DS","CGPA":8.5},"student 1":{"name":"Saivivek","branch" : "AI&ML","CGPA":8.6},"student 3":{"name":"Saivinay","branch" : "AI","CGPA":7.0}}
for key,value in dici.items():
    print(f"{key} : name = {value["name"]}")
    print(f"{key} : branch ={value["branch"]}")
    print(f"{key} : CGPA ={value["CGPA"]}")