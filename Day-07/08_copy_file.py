with open("example.txt","r") as f:
    data=f.read()
    with open("example_1.txt","w") as f1:
        f1.write(data)