def get_countries_updated(country_1, state_1):
    countries = {"USA": {"California": {"Los Angeles": 4000000, "San Francisco": 870000}},
                 "Canada": {"Ontario": {"Toronto": 2930000, "Ottawa": 994837}}
                 }
    for country,state in countries.items():
        print("country: \t", country, "\nState: \t", state)
        for each,value in state.items():
            print("\nEach: \t", each, "\nValue: \t", value)
            if country != country_1 and state != state_1:
                print("\nCountry and State updated successfully!")
                countries[country_1] = state_1
                print(countries)
                return " "



def get_valid_nigeria_input(message):
    valid_input = False
    while not valid_input:
        response = input(message).strip()
        if response == "nigeria".casefold():
            return response
        else:
            print("Invalid input. Please enter a non-empty string or 'nigeria'")
country = get_valid_nigeria_input("Enter country: ")
state = input("Enter state: ")

print(get_countries_updated(country, state))
