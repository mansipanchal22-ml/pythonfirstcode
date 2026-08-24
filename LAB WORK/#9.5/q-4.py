#q-4 Bank Account Management System
# Objective:
# Demonstrate all four OOP principles through a simple financial simulation.

#Encapsulation:
# -Create a class BankAccount with private attributes:
#  -account_number
#  -balance
# -Provide methods:
#  -deposit()
#  -withdraw()
#  -get_balance()
# -These methods control access to balance safely.

# Inheritance:
# -Create a subclass SavingsAccount that inherits from BankAccount.
# -Add an additional attribute interest_rate and method add_interest().
# Polymorphism:
# -Create another subclass CurrentAccount with an overridden withdraw() method that allows overdraft up to a limit.
# Abstraction:
# -Define an abstract class Account from abc module with abstract methods deposit() and withdraw().
# -Both SavingsAccount and CurrentAccount should inherit from this abstract class.
# Test Section:
# -Create objects of both account types.
# -Perform deposits, withdrawals, and display balance with interest calculations.

from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class BankAccount(Account):
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return "Amount deposited successfully"
        return "Invalid amount"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return "Amount withdrawn successfully"
        return "Insufficient balance"

    def get_balance(self):
        return self.__balance

    def _set_balance(self, balance):
        self.__balance = balance

class SavingsAccount(BankAccount):

    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        return interest

class CurrentAccount(BankAccount):

    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):

        if amount <= self.get_balance() + self.overdraft_limit:
            new_balance = self.get_balance() - amount
            self._set_balance(new_balance)
            return "Amount withdrawn successfully"

        return "Overdraft limit exceeded"

# Savings Account
savings = SavingsAccount("S001", 10000, 5)

print("----- Savings Account -----")

print(savings.deposit(2000))
print(savings.withdraw(3000))
print("Interest Added:", savings.add_interest())
print("Balance:", savings.get_balance())

print()

# Current Account
current = CurrentAccount("C001", 5000, 3000)

print("----- Current Account -----")

print(current.deposit(2000))
print(current.withdraw(9000))
print("Balance:", current.get_balance())