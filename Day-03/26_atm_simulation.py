balance=10000
que=int(input(("For check balance:Enter 1 Withdraw money:Enter 2,Deposit money:Enter 3")))
if que==1:
    print("The balance is :",balance)
elif que==2:
    withdraw_amount=int(input("How much amount to withdraw :"))
    if withdraw_amount<=balance:
        print("Withdraw successfully")
        print("Updated balance:",balance-withdraw_amount)
elif que==3:
    deposit_amount=int(input("How much amount to Deposit :"))
    print("Updated balance:",balance+deposit_amount)