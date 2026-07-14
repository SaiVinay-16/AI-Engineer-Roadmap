balance = 10000  

withdraw_amount = int(input("Enter the amount to withdraw: "))

if withdraw_amount <= balance:
    balance -= withdraw_amount
    print("Transaction successful!")
    print("Updated balance: ₹", balance)
else:
    print("Transaction failed! Insufficient balance.")
    print("Available balance: ₹", balance)
