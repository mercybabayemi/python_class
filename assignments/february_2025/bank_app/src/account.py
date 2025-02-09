class Account:
    def __init__(self, first_name, last_name, pin):
        self.pin = pin
        self.balance = 0
        self.account_number = 0
        self.first_name = first_name
        self.last_name = last_name

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount must be a positive number")
        self.balance += amount

    def get_balance(self, pin):
        if self.pin == pin:
            return self.balance
        else:
            raise ValueError("PIN does not match")

    def withdraw(self, amount, pin_input):
        if amount > self.balance or amount < 0:
            raise ValueError("Amount must be greater than zero and less than or equal to balance.")
        if pin_input == self.pin:
            self.balance -= amount
        else:
            raise ValueError("PIN does not match.")

    def update_pin(self, old_pin, new_pin):
        if not self.pin:
            raise ValueError("PIN is empty.")
        if not old_pin or not new_pin:
            raise ValueError("Old or new pin cannot be empty.")
        if old_pin == self.pin:
            self.pin = new_pin
        else:
            raise ValueError("PIN does not match.")

    def update_first_name(self, old_name, new_name):
        if not self.first_name:
            raise ValueError("First name is empty.")
        if not old_name or not new_name:
            raise ValueError("Old or new first name cannot be empty.")
        if old_name == self.first_name:
            self.first_name = new_name
        else:
            raise ValueError("First name does not match.")

    def __str__(self):
        return f"Account Name: {self.first_name} {self.last_name}\nAccount Balance: {self.balance}\nAccount Number: {self.account_number}"

    def get_account_number(self):
        return self.account_number
