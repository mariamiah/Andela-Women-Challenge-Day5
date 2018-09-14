class BankAccount:
    def __init__(self, number):
        self.balance = 0
        self.number = number
        self.accounts = {}
        
    def get_balance(self):
        if self.number not in self.accounts.values():
            raise ValueError("Cannot query balance of closed account")
        return self.balance

    def open(self):
        self.accounts['number'] = self.number

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Cannot deposit negative amount")
        self.balance = self.balance + amount

        if self.number not in self.accounts.values():
            raise ValueError("Cannot deposit into closed account")
          
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Funds not enough")
        self.balance = self.balance - amount

        if amount < 0:
            raise ValueError("cannot withdraw negative funds")

    def close(self):
        del self.accounts['number']

