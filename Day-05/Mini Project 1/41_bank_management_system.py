balance = 0.0

def check_balance():
    print("Current Balance: ₹", balance)

def deposit(amount):
    global balance
    balance += amount
    print("₹", amount, "deposited successfully.")
    check_balance()

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print("₹", amount, "withdrawn successfully.")
        check_balance()

def bank_system():
    while True:
        print("\n--- Bank Management System ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            check_balance()
        elif choice == '2':
            amt = float(input("Enter amount to deposit: "))
            deposit(amt)
        elif choice == '3':
            amt = float(input("Enter amount to withdraw: "))
            withdraw(amt)
        elif choice == '4':
            print("Thank you for using the Bank Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

bank_system()