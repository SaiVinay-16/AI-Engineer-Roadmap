salary = float(input("Enter your salary: ₹"))

if salary < 30000:
    bonus = salary * 0.20
elif salary <= 60000:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05

print("Your bonus amount is: ₹", round(bonus, 2))