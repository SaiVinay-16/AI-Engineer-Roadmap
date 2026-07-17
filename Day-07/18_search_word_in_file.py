def check_word():
    with open("example.txt","r") as f:
        word=input("Enter the word:").strip().lower()
        data=f.readlines()
        for line in data:
            temp=line.lower().split()
            if word in temp:
                return "Word Found"
        return "Word Not Found"
print(check_word())