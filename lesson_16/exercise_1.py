# Class
# Define a class named BankAccount with an __init__ method that initializes two
# instance variables: account_holder and balance.
# The class has methods like deposit and withdraw, each of which takes an amount as
# an argument and updates the account balance accordingly. These methods also
# include checks for valid input and available funds.
# The get_balance method allows you to retrieve the account balance.
# We create an Object of the BankAccount class called account1 with an initial balance
# of $1000.
# We deposit $500 and withdraw $200 from the account and print the account
# information.

class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if type(amount) is not int:
            raise Exception("Enter digit!!!")
        self.balance += amount

    def withdraw(self, amount):
        if not isinstance(amount, int) or not isinstance(amount, float):
            raise Exception("Enter digit!!!")
        if amount > self.balance:
            raise Exception("Insufficient funds")
        self.balance -= amount

    def get_balance(self):
        print(f"name : {self.account_holder}\nbalance = {self.balance}")


account_1 = BankAccount("Arman", 1000)
account_1.deposit(500)
account_1.withdraw("bbb")
account_1.get_balance()
