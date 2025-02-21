from geo_political_zone import GeoPoliticalZONES


def find_state_zones(user_input, self = GeoPoliticalZONES):
    return GeoPoliticalZONES.get_state(self,user_input)


def display_result(found_zones, user_input):
    if found_zones:
        print(f"The geo political zone for {user_input} state is {found_zones}")
    else:
        print("Matching states not found in zones. Try Again")


def main_menu():
        validated = False

        while not validated:
            print("Which state are you from in Nigeria? ")
            user_input = validate_string_input("Enter response: ")
            found_zones = find_state_zones(user_input)
            if found_zones:
                display_result(found_zones, user_input)
                validated = True
            else:
                display_result(found_zones, user_input)


def validate_string_input(prompt="Enter input: "):
    user_input = ""
    valid = False
    while not valid:
        user_input = input(prompt).strip()
        if not user_input or " " in user_input:
            print("Input cannot be empty or contain spaces.")
            continue
        valid = True
    return user_input


if __name__ == '__main__':
    main_menu()