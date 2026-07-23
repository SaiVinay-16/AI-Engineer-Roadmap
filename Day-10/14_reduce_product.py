from functools import reduce
li=[34,89,22,88,75,43]
result=reduce(lambda x,y:x*y,li)
print(result)