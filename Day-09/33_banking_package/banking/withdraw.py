def withdraw(balance, amount):
    """Withdraw amount from balance."""
    if amount <= 0:
        print("❌ Withdrawal amount must be positive.")
    elif amount > balance:
        print("❌ Insufficient funds.")
    else:
        balance -= amount
        print(f"✅ Withdrew ₹{amount}. New balance: ₹{balance}")
    return balance
