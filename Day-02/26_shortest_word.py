st=input("Enter the sentence to find the shortest word:")
res=""
for word in st.split():
    if len(res)==0:
        res=word
    if len(word)<len(res):
        res=word
print(res)