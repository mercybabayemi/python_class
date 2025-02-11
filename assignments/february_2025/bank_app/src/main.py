from account import Account
from bank import Bank


def main_menu():
    bank = Bank(Account("Mercy", "Janet", "1234"))
    menu(bank)


def menu(bank):
        print("\nMain Menu:")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            pin = input("Enter PIN: ")
            account_number = bank.create_account(first_name, last_name, pin)
            print(f"Account created successfully! Account number: {account_number}")
            menu(bank)

        elif choice == "2":
            account_number = int(input("Enter Account Number: "))
            pin = input("Enter PIN: ")
            try:
                balance = bank.check_balance(account_number, pin)
                print(f"Balance: {balance}")
            except ValueError as e:
                print(f"Error: {e}")
            menu(bank)

        elif choice == "3":
            account_number = int(input("Enter Account Number: "))
            amount = int(input("Enter Amount to Deposit: "))
            try:
                bank.deposit(account_number, amount)
                print(f"Deposited {amount} successfully!")
            except ValueError as e:
                print(f"Error: {e}")
            menu(bank)

        elif choice == "4":
            account_number = int(input("Enter Account Number: "))
            amount = int(input("Enter Amount to Withdraw: "))
            pin = input("Enter PIN: ")
            try:
                bank.withdraw(account_number, amount, pin)
                print(f"Withdrawn {amount} successfully!")
            except ValueError as e:
                print(f"Error: {e}")
            menu(bank)

        elif choice == "5":
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

        elif choice == "6":
            print("Exiting the system.")

        else:
            print("Invalid choice! Please select again.")
            main_menu()

if __name__ == '__main__':
    main_menu()