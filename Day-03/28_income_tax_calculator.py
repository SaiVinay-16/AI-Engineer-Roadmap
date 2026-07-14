# 28_income_tax_calculator.py

income = int(input("Enter your annual income: "))

tax = 0

# Example slab values (you can change them for practice):
# Up to 2,50,000 → No tax
# 2,50,001 – 5,00,000 → 5%
# 5,00,001 – 10,00,000 → 20%
# Above 10,00,000 → 30%

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = (250000 * 0.05) + (income - 500000) * 0.20
else:
    tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30

print("\n--- Income Tax Calculation ---")
print("Annual Income: ₹", income)
print("Calculated Tax: ₹", tax)