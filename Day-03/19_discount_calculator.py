amount = float(input("Enter the amount: ₹"))
if amount>=5000:
    amount=amount-amount*0.2    
elif 2000<=amount<=4999:
    amount=amount-amount*0.1
print("Your final bill is: ₹", round(amount, 2))