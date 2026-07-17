name=input("Enter the name:")
age=int(input("Enter the age:"))
with open("sample_02.txt","w") as f:
    f.write(f"Name : {name} \n")
    f.write(f"Age : {age}")
with open("sample_02.txt","r") as f:
    data=f.read()
    print(data)