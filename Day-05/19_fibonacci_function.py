def fibonacci_function(num):
    li=[0,1]
    if num==1:
        print(li[0])
    elif num==2:
        print(li)
    else:
        for i in range(2,num):
            li.append(li[i-1]+li[i-2])
    return " ".join(str(i) for i in li)
num=int(input("Enter the number:"))
print(fibonacci_function(num))