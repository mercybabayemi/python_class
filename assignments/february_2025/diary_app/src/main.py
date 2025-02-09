from diary import Diary


def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    diary = Diary(username, password)
    main_menu(diary)

def main_menu(diary):
    print("\nDiary Menu:")
    print("1. Add a new entry")
    print("2. View all entries")
    print("3. Delete an entry")
    print("4. Exit")

    choice = input("Please choose an option (1-4): ")

    if choice == "1":
        title = input("Enter the title of the entry: ")
        content = input("Enter the content of the entry: ")
        diary.add_entry(title, content)
        print("Entry added.")
        main_menu(diary)

    elif choice == "2":
        diary.view_entries()

    elif choice == "3":
        diary.view_entries()
        try:
            index = int(input("Enter the entry number to delete: ")) - 1
            diary.delete_entry(index)
        except ValueError:
            print("Please enter a valid number.")
        main_menu(diary)

    elif choice == "4":
        print("Goodbye!")

    else:
        print("Invalid choice. Please try again.")
        main_menu(diary)

if __name__ == "__main__":
    main()