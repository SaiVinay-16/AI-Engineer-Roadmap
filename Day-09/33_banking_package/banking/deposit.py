def deposit(balance, amount):
    """Deposit amount into balance."""
    if amount <= 0:
        print("❌ Deposit amount must be positive.")
        return balance
    balance += amount
    print(f"✅ Deposited ₹{amount}. New balance: ₹{balance}")
    return balance
