from banking import deposit,balance,withdraw
print("1.Deposit")
print("2.withdraw")
print("3.Display balance")
choice=int(input("Enter your choice(1/2/3):"))
if choice==1:
    print(deposit.deposit(10000,2222))
elif choice==2:
    print(withdraw.withdraw(5000,4999))
elif choice==3:
    print(balance.show_balance(3000))
else:
    print("Invalid choice")