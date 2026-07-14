base=int(input("Enter the base:"))
power=int(input("Enter the power:"))
res=base
for i in range(power-1):
    res*=base
print("Answer:",res)