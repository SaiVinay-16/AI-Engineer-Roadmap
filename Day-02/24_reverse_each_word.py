string1=input("Enter the string:")
for word in string1.split():
    word=word[-1::-1]
    print(word,end=" ")