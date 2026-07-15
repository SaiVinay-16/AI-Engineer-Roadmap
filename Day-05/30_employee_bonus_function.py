def calculate_bonus(salary):
    if salary < 30000:
        return salary * 0.20
    elif 30000 <= salary <= 60000:
        return salary * 0.10
    else:
        return salary * 0.05
salary=int(input("Enter your salary:"))
print(calculate_bonus(salary))