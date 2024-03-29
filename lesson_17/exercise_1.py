# Exercise: Bank Account Hierarchy
# Create a hierarchy of classes representing different types of bank accounts. Start
# with a base class called BankAccount. Then, create two subclasses,
# SavingsAccount and CheckingAccount. Each subclass should inherit from the
# BankAccount class.
# ● The BankAccount class should have the following attributes and methods:
# ○ Attributes: account_number, balance
# ○ Methods: __init__ (constructor), deposit, withdraw, and get_balance
# ● The SavingsAccount class should inherit from BankAccount and have an
# additional attribute interest_rate. Override the deposit method to add
# interest to the balance when a deposit is made.
# ● The CheckingAccount class should inherit from BankAccount and have an
# additional attribute overdraft_fee. Override the withdraw method to deduct
# the overdraft fee if a withdrawal causes the balance to go below zero.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account = account_number
        self.account_balance = balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        self.account_balance -= amount

    def get_balance(self):
        return f"Username : {self.account}\nBalance : {self.account_balance}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.account_balance += amount + (amount*(self.interest_rate/100))
        return self.account_balance


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_fee):
        super().__init__(account_number, balance)
        self.interest_rate = overdraft_fee

    def withdraw(self, amount):
        if amount > self.account_balance:
            self.account_balance -= amount + self.interest_rate
        return self.account_balance


x = SavingsAccount('aaa', 0, 10)
x.deposit(100)
print(x.get_balance())
