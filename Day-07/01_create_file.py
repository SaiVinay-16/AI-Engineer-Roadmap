with open("sample_01.txt","w") as f:
    f.write("Welcome to Python File Handling.")
with open("sample_01.txt","r") as f:
    data=f.read()
    print(data)