class ATM:
    def __init__(self, balance ):
        self.__balance = balance


    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount} | New Balance: {self.__balance}")  

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount} | Remaining Balance: {self.__balance}")
        else:
            print("Insufficient balance for withdrawal.")   

    def check_balance(self):
        print(f"Current Balance: {self.__balance}")      

a1 = ATM(1000)   

a1.deposit(500)
a1.withdraw(200)
a1.withdraw(2000)
a1.check_balance()