num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
greater=max(num1,num2)
while True:
    if greater % num1==0 and greater %num2==0:
        lcm=greater
        break
    greater+=1
print("lcm:",lcm)