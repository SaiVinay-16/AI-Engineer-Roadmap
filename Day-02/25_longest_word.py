st=input("Enter the sentence to find the longest word:")
res=""
for word in st.split():
    if len(word)>len(res):
        res=word
print(res)