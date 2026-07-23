from functools import reduce
li=[34,89,22,88,75,43]
result=reduce(lambda temp,x:temp if temp>x else x,li)
print(result)