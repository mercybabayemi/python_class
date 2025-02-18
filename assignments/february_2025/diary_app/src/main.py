import sys
from diaries import Diaries

class Main:
    def __init__(self):
        self.diaries = Diaries()
        self.diary = None

    def main_menu(self):
        self.display_welcome()
        self.users_choice()

    def display_welcome(self):
        print("""
            Welcome to Diaries
            --- Main Menu ---
            1. Create a new diary
            2. Login to existing diary
            3. Show all diaries
            4. Delete diary from diaries
            5. Exit
            Enter your choice:
        """)

    def users_choice(self):
        choice = self.validate_int_input()

        if choice == 1:
            self.create_diary()
        elif choice == 2:
            self.login_to_existing_diary()
        elif choice == 3:
            self.show_all_diaries()
        elif choice == 4:
            self.delete_diary()
        elif choice == 5:
            self.exit()
        else:
            print("Invalid choice. Please try again.")
            self.main_menu()

    def delete_diary(self):
        username = self.validate_string_input("Enter username: ")
        password = self.validate_string_input("Enter password: ")
        try:
            self.diaries.delete(username, password)
            print("Diary deleted.")
        except Exception as e:
            print(e)
        self.main_menu()

    def show_all_diaries(self):
        if not self.diaries.get_all_diaries():
            print("No diaries available.")
        else:
            for diary in self.diaries.get_all_diaries():
                print(diary)
        self.main_menu()

    def create_diary(self):
        username = self.validate_string_input("Enter username: ")
        password = self.validate_string_input("Enter password: ")
        self.diaries.add(username, password)
        print("Diary created successfully!")
        self.main_menu()

    def login_to_existing_diary(self):
        username = self.validate_string_input("Enter username: ")
        password = self.validate_string_input("Enter password: ")
        try:
            existing_diary = self.diaries.find_by_username(username)
            if existing_diary.get_is_locked():
                existing_diary.unlock_diary(password)
            self.diary = existing_diary
            self.diary_entry_menu(existing_diary)
        except Exception as e:
            print(e)
        self.main_menu()

    def diary_entry_menu(self, existing_diary):
        if self.diary is None:
            print("You need to log in first.")
            return
        self.display_diary_welcome()
        self.diary_choice()

    def display_diary_welcome(self):
        print("""
            ---- Diary Menu ----
            1. Create New Entry
            2. View Entry
            3. View Entries
            4. Update Entry
            5. Delete Entry
            6. Lock Diary
            7. Logout
            Enter your choice:
        """)

    def diary_choice(self):
        choice = self.validate_int_input()

        if choice == 1:
            self.create_entry()
        elif choice == 2:
            self.view_entry()
        elif choice == 3:
            self.view_entries()
        elif choice == 4:
            self.update_entries()
        elif choice == 5:
            self.delete_entry()
        elif choice == 6:
            self.lock_entry()
        elif choice == 7:
            self.logout()
        else:
            print("Invalid choice. Please try again.")
            self.diary_choice()

    def logout(self):
        print("Logging out>>>")
        self.main_menu()

    def validate_lock_and_unlock_diary(self):
        while self.diary.get_is_locked():
            print("Unlock diary to continue.")
            self.unlock_entry()

    def unlock_entry(self):
        password = self.validate_string_input("Enter password: ")
        try:
            self.diary.unlock_diary(password)
            print("Diary is unlocked.")
        except Exception as e:
            print(e)

    def lock_entry(self):
        try:
            self.diary.lock_diary()
            print("Diary is locked.")
        except Exception as e:
            print(e)
        self.diary_entry_menu(self.diary)

    def delete_entry(self):
        self.validate_lock_and_unlock_diary()
        entry_id = self.validate_int_input("Enter entry ID to delete: ")
        try:
            self.diary.delete_entry(entry_id)
            print("Entry deleted.")
        except Exception as e:
            print(e)
        self.diary_entry_menu(self.diary)

    def update_entries(self):
        self.validate_lock_and_unlock_diary()
        entry_id = self.validate_int_input("Enter entry ID to update: ")
        new_title = self.validate_string_input("Enter new title: ")
        new_body = self.validate_string_input("Enter new body: ")
        try:
            self.diary.update_entry(entry_id, new_title, new_body)
            print("Entry updated.")
        except Exception as e:
            print(e)
        self.diary_entry_menu(self.diary)

    def view_entry(self):
        self.validate_lock_and_unlock_diary()
        entry_id = self.validate_int_input("Enter entry ID to view: ")

        try:
            self.diary.view_entry(entry_id)
        except Exception as e:
            print("Diary entry not found")
        self.diary_entry_menu(self.diary)

    def view_entries(self):
        self.validate_lock_and_unlock_diary()
        print("-----Entries-----")
        try:
            for i in range(1, self.diary.size() + 1):
                entry = self.diary.find_entry_by_id(i)
                print(entry)
            if self.diary.size() == 0:
                print("Diary is empty")
        except Exception as e:
            print(e)
        self.diary_entry_menu(self.diary)

    def create_entry(self):
        self.validate_lock_and_unlock_diary()
        title = self.validate_string_input("Enter title: ")
        body = self.validate_string_input("Enter body: ")
        entry_id = self.diary.create_entry(title, body)
        print(f"Entry ID: {entry_id}")
        print("Entry created successfully!")
        self.diary_entry_menu(self.diary)

    def exit(self):
        print("Goodbye!!!")
        sys.exit(0)

    def validate_int_input(self, prompt="Enter choice: "):
        valid = False
        user_input = ""

        while not valid:
            try:
                user_input = input(prompt).strip()
                if not user_input.isdigit():
                    print("Invalid input. Please enter an integer.")
                    continue
                valid = True
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        return int(user_input)

    def validate_string_input(self, prompt="Enter input: "):
        user_input = ""
        valid = False
        while not valid:
            user_input = input(prompt).strip()
            if not user_input or " " in user_input:
                print("Input cannot be empty or contain spaces.")
                continue
            valid = True
        return user_input


if __name__ == "__main__":
    app = Main()
    app.main_menu()
