#Q-5.Implement a class Account with a private attribute balance.
# -Create methods to deposit and withdraw money.
# -Add a method to display the balance.
# -Ensure balance cannot be accessed directly.

class Account:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance = self.__balance - amount
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print("Balance:", self.__balance)

a1 = Account(5000)

a1.deposit(2000)

a1.withdraw(1000)

a1.display_balance()