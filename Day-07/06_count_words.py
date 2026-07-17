with open("example.txt","r") as f:
    data=f.readlines()
    count=0
    for line in data:
        temp=line.split()
        count+=len(temp)
    print(count)