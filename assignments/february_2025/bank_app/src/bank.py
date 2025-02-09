from account import Account
from arraylist_method import ArrayListMethod


class Bank:
    def __init__(self):
        self.accounts = ArrayListMethod()
        self.account_count = 0

    def is_accounts_empty(self):
        return self.accounts.is_empty()

    def add(self, account):
        self.accounts.add(account)

    def get_size(self):
        return self.accounts.size()

    def remove(self, account_number):
        self.accounts.remove(account_number)

    def create_account(self, first_name, last_name, pin):
        account = Account(first_name, last_name, pin)
        account_number = self.generate_account_number()
        account.set_account_number(account_number)
        self.accounts.add(account)
        return account.get_account_number()

    def generate_account_number(self):
        self.account_count += 1
        return self.account_count

    def clear(self):
        self.accounts.remove_all()
        return self

    def find_account_by_account_number(self, account_number):
        if account_number < 1 or account_number > self.account_count:
            raise ValueError("Account number does not exist")
        return self.accounts.get(account_number - 1)

    def check_balance(self, account_number, pin):
        account = self.find_account_by_account_number(account_number)
        return account.get_balance(pin)

    def deposit(self, account_number, amount):
        account = self.find_account_by_account_number(account_number)
        account.deposit(amount)

    def withdraw(self, account_number, amount, pin):
        account = self.find_account_by_account_number(account_number)
        account.withdraw(amount, pin)

    def transfer(self, sender_account, receiver_account, amount, pin):
        if sender_account == receiver_account:
            raise ValueError("Cannot transfer from the same account")
        sender = self.find_account_by_account_number(sender_account)
        receiver = self.find_account_by_account_number(receiver_account)
        sender.withdraw(amount, pin)
        receiver.deposit(amount)
