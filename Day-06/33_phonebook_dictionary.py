dici={"Saivinay":9032328316,"Lakshmi":9989913643}
print("1.Add Contact")
print("2.Search Contact")
print("3.Display All Contacts")
print("Enter your choice(1/2/3) :")
n=int(input())
if n==1:
    key=input("Enter the name:")
    value=int(input("Enter the number:"))
    dici[key]=value
elif n==2:
    temp=input("Enter the name:")
    if temp in dici.keys():
        print(f"{temp} : {dici[temp]}")
    else:
        print("Name not found")
elif n==3:
    for x,y in dici.items():
        print(f"{x} : {y}")
else:
    print("Your entered wrong choice")