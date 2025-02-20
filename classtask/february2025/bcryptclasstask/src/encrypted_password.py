import bcrypt

USER_DETAILS = 'user_details.txt'

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def save_to_file(username, hashed_password):
    with open(USER_DETAILS, 'a') as file:
        file.write(f'{username}:{hashed_password.decode("utf-8")}\n')

def register_user():
    while True:
        username = input("Enter your username: ")
        if not username:
            print("Username cannot be empty.")
            continue
        break

    while True:
        password = input("Enter your password: ")
        if not password:
            print("Password cannot be empty.")
            continue
        break

    save_to_file(username, hash_password(password))
    print('User registered successfully')

def validate_user(username, password):
    with open(USER_DETAILS, 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(':')
            if username == stored_username:
                return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))

    # with open(USER_DETAILS, 'r') as file:
    #     details = file.read()
    #     if not details:
    #         print("No registered users found")
    #         return False
    #     for line in details.split('\n'):
    #         if line.strip():
    #             stored_username, stored_password = line.split(',')
    #             if username == stored_username:
    #                 if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
    #                     return True
    # return False

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if validate_user(username, password):
        print("Login successful!")
    else:
        print("Invalid username or password")


def main():
    menu = """
    1. Register user
    2. Login user
    3. Exit
    """
    while True:
        choice = input(menu)

        match choice:
            case '1':
                register_user()
            case '2':
                login_user()
            case '3':
                print('Thank you')
                break



main()