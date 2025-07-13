from abc import ABC, abstractmethod  # For abstraction

# Abstract Base Class
class Account(ABC):
    def __init__(self, account_number, balance):
        self.__account_number = account_number   # Encapsulation
        self.__balance = balance                 # Encapsulation

    # Encapsulated getter
    def get_balance(self):
        return self.__balance

    # Encapsulated deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}")
        else:
            print("Invalid amount")

    # Encapsulated withdraw method with simple logic
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}")
        else:
            print("Insufficient balance")

    # Abstract method for interest calculation (Polymorphism)
    @abstractmethod
    def calculate_interest(self):
        pass

# Subclass: Savings Account
class SavingsAccount(Account):
    def calculate_interest(self):
        interest = self.get_balance() * 0.04  # 4% interest
        return interest

# Subclass: Current Account
class CurrentAccount(Account):
    def calculate_interest(self):
        return 0  # No interest for current accounts

# ---------- Testing the code ----------

print("---- Savings Account ----")
s1 = SavingsAccount(account_number=101, balance=1000)
s1.deposit(500)
s1.withdraw(200)
print("Balance:", s1.get_balance())
print("Interest:", s1.calculate_interest())

print("\n---- Current Account ----")
c1 = CurrentAccount(account_number=102, balance=5000)
c1.deposit(1000)
c1.withdraw(7000)
print("Balance:", c1.get_balance())
print("Interest:", c1.calculate_interest())
