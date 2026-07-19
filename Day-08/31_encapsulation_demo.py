class BankAccount:
    __balance=10000
    def __deposit(self):
        self.__depo=int(input("Enter the deposit amount:"))
        self.__balance+=self.__depo
    def __withdraw(self):
        self.__withdraw=int(input("Enter the withdraw amount:"))
        if self.__withdraw > self.__balance:
            print("Amount Exceeded")
        else:
            self.__balance-=self.__withdraw
    def __display(self):
        print(f"Balance : {self.__balance}")
    def withdraw(self):
        self.__withdraw()
    def deposit(self):
        self.__deposit()
    def get_details(self):
        self.__display()
obj=BankAccount()
obj.deposit()
obj.get_details()