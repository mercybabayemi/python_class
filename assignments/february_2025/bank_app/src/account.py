class Account:
    def __init__(self, first_name: str, last_name:str, pin:str) -> None:
        self._pin = pin
        self._balance = 0
        self._account_number = 0
        self._first_name = first_name
        self._last_name = last_name

    def update_first_name(self, old_name:str, new_name:str) -> None:
        if not self._first_name:
            raise ValueError("First name is empty.")
        if not old_name or not new_name:
            raise ValueError("Old or new first name cannot be empty.")
        if old_name == self._first_name:
            self._first_name = new_name
        else:
            raise ValueError("First name does not match.")

    def deposit(self, amount:float) -> None:
        if amount < 0:
            raise ValueError("Amount must be a positive number")
        self._balance += amount

    def get_balance(self, pin:str) -> int:
        if pin not in self._pin:
            raise ValueError("Invalid pin number.")
        else:
            return self._balance

    def withdraw(self, amount:float, pin_input: str) -> None:
        if amount > self._balance or amount < 0:
            raise ValueError("Amount must be greater than zero and less than or equal to balance.")
        if pin_input == self._pin:
            self._balance -= amount
        else:
            raise ValueError("PIN does not match.")

    def update_pin(self, old_pin:str, new_pin:str) -> None:
        if not self._pin:
            raise ValueError("PIN is empty.")
        if not old_pin or not new_pin:
            raise ValueError("Old or new pin cannot be empty.")
        if old_pin == self._pin:
            self._pin = new_pin
        else:
            raise ValueError("PIN does not match.")

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f"Account Name: {self._first_name} {self._last_name}\nAccount Balance: {self._balance}\nAccount Number: {self._account_number}"
    