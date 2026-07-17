with open("sample_05.txt","r") as f:
    data=f.readlines()
    for line in reversed(data):
        print(line)