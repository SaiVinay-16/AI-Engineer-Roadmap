balance=15000
print("Check Balance : Enter 1")
print("Deposit : Enter 2")
print("Withdraw :Enter 3")
print("Exit :Enter 4")
choice=int(input("Enter the number based on your choice : "))
if str(choice).isdigit() and choice<=4:
    if choice ==1:
        print("The available balance : ",balance)
    elif choice==2:
        deposit_amount=int(input("How much amount to deposit : "))
        print("The Updated balance : ",balance+deposit_amount)
    elif choice==3:
        withdraw_amount=int(input("How much amount to withdraw : "))
        if withdraw_amount<=balance:
            print("The Updated balance : ",balance-withdraw_amount)
        else:
            print("Withdraw amount is higher than available balance")
            print("The available balance : ",balance)
    elif choice == 4:
        print("======Exit======")
else:
    print("Invalid number(Enter the number between 1-4)")