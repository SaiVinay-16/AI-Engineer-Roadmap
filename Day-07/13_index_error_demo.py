try:
    li=[11,22,33,44]
    ind=int(input("Enter the index number:"))
    if not 0<=ind<len(li):
        raise IndexError("Index error")
except IndexError as e:
    print("Index out of bound :",e)
else:
    print(li[ind])
finally:
    print("==========================")