with open("sample_05.txt","r") as f:
    count=0
    data=f.readlines()
    for line in data:
        count+=1
    print(count)