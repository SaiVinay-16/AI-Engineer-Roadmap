slab=float(input("Enter the slab for the bill:"))
res=0
if slab<=100:
    res+=slab *3
elif 101<=slab<=200:
    res+=100*3
    slab-=100
    res+=slab*5
elif slab>200:
    res+=100*3
    res+=100*5
    slab-=200
    res+=slab*8
print(res)