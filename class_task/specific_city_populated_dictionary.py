def get_city_population(country, state):
    countries = {"USA": {"California": {"Los Angeles": 4000000, "San Francisco": 870000}},
                 "Canada": {"Ontario": {"Toronto": 2930000, "Ottawa": 994837}}
                 }
    for country in countries.values():
        for value in country.values():
            print("Los Angeles: ", value.get("Los Angeles"))
            print("San Francisco: ", value.get("San Francisco"))
            return " "

print(get_city_population("USA", "California"))