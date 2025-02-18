from account import Account
from bank import Bank


def main_menu():
    bank = Bank()
    menu(bank)


def menu(bank):
        display_welcome()
        users_choice(bank)

def display_welcome():
    print("\nMain Menu:")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Transfer")
    print("6. Exit")

def create_account(bank):
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    pin = input("Enter PIN: ")
    account_number = bank.create_account(first_name, last_name, pin)
    print(f"Account created successfully! Account number: {account_number}")
    menu(bank)

def check_balance(bank):
    account_number = int(input("Enter Account Number: "))
    pin = input("Enter PIN: ")
    try:
        balance = bank.check_balance(account_number, pin)
        print(f"Balance: {balance}")
    except ValueError as e:
        print(f"Error: {e}")
    menu(bank)

def deposit(bank):
    account_number = int(input("Enter Account Number: "))
    amount = int(input("Enter Amount to Deposit: "))
    try:
        bank.deposit(account_number, amount)
        print(f"Deposited {amount} successfully!")
    except ValueError as e:
        print(f"Error: {e}")
    menu(bank)

def withdraw(bank):
    account_number = int(input("Enter Account Number: "))
    amount = int(input("Enter Amount to Withdraw: "))
    pin = input("Enter PIN: ")
    try:
        bank.withdraw(account_number, amount, pin)
        print(f"Withdrawn {amount} successfully!")
    except ValueError as e:
        print(f"Error: {e}")
    menu(bank)

def transfer(bank):
    sender_account = int(input("Enter Sender Account Number: "))
    receiver_account = int(input("Enter Receiver Account Number: "))
    amount = int(input("Enter Amount to Transfer: "))
    pin = input("Enter PIN: ")
    try:
        bank.transfer(sender_account, receiver_account, amount, pin)
        print(f"Transferred {amount} successfully!")
    except ValueError as e:
        print(f"Error: {e}")
    menu(bank)
def exit_menu():
    print("Exiting the system.")

def users_choice(bank):
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        create_account(bank)

    elif choice == "2":
        check_balance(bank)

    elif choice == "3":
        deposit(bank)

    elif choice == "4":
        withdraw(bank)

    elif choice == "5":
        transfer(bank)

    elif choice == "6":
        exit_menu()

    else:
        print("Invalid choice! Please select again.")
        main_menu()

if __name__ == '__main__':
    main_menu()