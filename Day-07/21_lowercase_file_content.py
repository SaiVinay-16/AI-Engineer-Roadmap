with open("sample_05.txt","r") as f:
    data=f.readlines()
    for line in data:
        print(line.lower())