class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self):
        self.depo=int(input("Enter the amount to deposit:"))
        self.balance = self.balance+self.depo
    def withdraw(self):
        wd=int(input("Enter the amount to withdraw:"))
        if self.wd>self.balance:
            print("Withdraw amount is greater than balance!")
        else:
            self.balance-=self.wd
    def display(self):
        print(f"Balance : {self.balance}")
balance=10000
ba=BankAccount(balance)
ba.deposit()
ba.display()