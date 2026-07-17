with open("new.txt","w") as f:
    for i in range(2):
        name=input("Enter the name:")
        marks=int(input("Enter your marks:"))
        f.write(f"{name} : {marks} \n")
with open("new.txt","r") as h:
        data=h.readlines()
        print(data)