import re

from system import System


def validate_value_for_rating():
    while True:
        value_input = input("Enter a rate for the movie(1-5): ")
        if not re.fullmatch("[1-5]", value_input):
            print("Invalid input")
            print("Enter a valid choice")
        else:
            return int(value_input)


def validate_user_choice():
    while True:
        user_choice = input("Enter your choice: ")
        if not re.fullmatch("[1-6]", user_choice):
            print("Invalid input")
            print("Enter a valid choice")
        else:
            return user_choice


class Main:

    def __init__(self):
        self.system = System()

    def display(self):
        print("""
        1.Add a movie
        2.Rate a movie
        3.View all available movies
        4.View a movie average rating
        5.View all movies average Ratings
        6. Exit the program
        """)

        user_choice = validate_user_choice()
        return user_choice

    def case_match(self, user_choice):
        match user_choice:
            case "1":
                try:
                    movie_name = input("Enter the movie name:").lower()
                    self.system.add_movie(movie_name)
                    self.main_menu()
                except Exception as e:
                    print("{}".format(e))
                    self.main_menu()

            case "2":
                try:
                    movie_name = input("Enter the movie name:").lower()
                    value = validate_value_for_rating()
                    self.system.rate_movie(movie_name, value)
                    self.main_menu()
                except Exception as e:
                    print("{}".format(e))
                    self.main_menu()

            case "3":
                try:
                    self.system.view_available_movies()
                    self.main_menu()
                except Exception as e:
                    print("{}".format(e))
                    self.main_menu()

            case "4":
                try:
                    movie_name = input("Enter the movie name:").lower()
                    self.system.get_movie_average_rating(movie_name)
                    self.main_menu()
                except Exception as e:
                    print("{}".format(e))
                    self.main_menu()
            case "5":
                try:
                    self.system.get_movies_average_rating()
                    self.main_menu()
                except Exception as e:
                    print("{}".format(e))
                    self.main_menu()
            case "6":
                print("""
                Thank you for using the program.
                We hope you enjoyed the movie.
                      """)

    def main_menu(self):
        choice = self.display()
        self.case_match(choice)

if __name__ == "__main__":
    main = Main()
    main.main_menu()