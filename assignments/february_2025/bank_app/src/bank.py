from typing import Any

from account import Account


class Bank:
    def __init__(self, account: Account):
        self.account = account
        self._accounts = []
        self._account_count = 0

    def is_accounts_empty(self) -> bool:
        if self._account_count == 0:
            return True
        else:
            return False

    def create_account(self, first_name, last_name, pin) -> int:
        creation = Account(first_name, last_name, pin)
        account_number = self.generate_account_number()
        creation.set_account_number(account_number)
        self.add_account(creation)
        return creation.get_account_number()

    def add_account(self, account):
        self._accounts.append(account)

    def generate_account_number(self):
        self._account_count += 1
        return self._account_count

    def get_size(self):
        return len(self._accounts)

    def remove(self, account_number):
        account_to_remove = self.find_account_by_account_number(account_number)
        if account_to_remove:
            self._accounts.remove(account_to_remove)
        else:
            raise ValueError(f"Account with account number {account_number} not found.")

    def find_account_by_account_number(self, account_number) -> Any | None:
        if int(account_number) < 1 or int(account_number) > self._account_count:
            raise ValueError("Account number does not exist")

        for account in self._accounts:
            if account.get_account_number() == account_number:
                return account

        return None

    def deposit(self, account_number, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        accountHere = self.find_account_by_account_number(account_number)
        accountHere.deposit(amount)

    def check_balance(self, account_number, pin):
        account = self.find_account_by_account_number(account_number)
        return account.get_balance(pin)

    def withdraw(self, account_number, amount, pin):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        for account in self._accounts:
            if pin != account._pin:
                raise ValueError("Pin number does not exist")
        account_found = self.find_account_by_account_number(account_number)
        account_found.withdraw(amount, pin)

    def transfer(self, sender_account, receiver_account, amount, pin):
        if sender_account == receiver_account:
            raise ValueError("Cannot transfer from the same account")
        sender = self.find_account_by_account_number(sender_account)
        receiver = self.find_account_by_account_number(receiver_account)
        sender.withdraw(amount, pin)
        receiver.deposit(amount)
