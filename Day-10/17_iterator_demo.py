try:
    li=[23,24,25,26]
    res=iter(li)
    print(next(res))
    print(next(res))
    print(next(res))
    print(next(res))
    print(next(res))
except StopIteration as s:
    print("No elements are there")