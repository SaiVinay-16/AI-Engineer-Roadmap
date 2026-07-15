def simple_interest(principal, time, rate):
    si = (principal * time * rate) / 100
    return si
principle=int(input("Enter the principal amount:"))
time=int(input("Enter the time:"))
rate=int(input("Enter the rate amount:"))
print(simple_interest(principle, time, rate))