from datetime import datetime

# from movie import Movie


class System:
    def __init__(self):
        self.date = datetime.now()
        self.movies = {}
        self.movie_count = 1
        self.ratings = []

    def add_movie(self, name):
        if name not in self.movies.values():
            self.movies[self.movie_count] = name
            self.movie_count += 1
            print("Movie added successfully")
        elif name in self.movies.values():
            raise ValueError("'{}' already exists".format(name))

    def get_movie(self, name):
        if name not in self.movies:
            return "Movie '{}' doesn't exist".format(name)
        else:
            return self.movies[name]


    def get_movie_by_id(self, value):
        if value not in self.movies:
            return f"Movie with index {value} doesn't exist"
        else:
            return self.movies[value]


    def rate_movie(self, movie_name, value):
        if movie_name not in self.movies.values():
            raise ValueError("Movie named '{}' doesn't exist".format(movie_name))
        elif type(value) is not int:
            raise ValueError("'{}' value is not an integer".format(value))
        else:
            movie_id = self.get_movie_by_id(movie_name)
            self.ratings.append([movie_id, movie_name, value])
            print("Movie '{}' has been rated successfully".format(movie_name))

    def get_movie_rating(self, movie_name):
        if movie_name not in self.movies.values():
            return "Movie '{}' doesn't exist".format(movie_name)
        else:
            for rating in self.ratings:
                if rating[1] == movie_name:
                    return rating[2]

    def view_available_movies(self):
        if not self.movies:
            print("No movies available.")
        else:
            print("Available movies:")
            for movie in self.movies.values():
                print(movie)

    def get_movie_average_rating(self, movie_name):
        movie_addition = 0
        count = 0
        if not self.movies:
            raise ValueError("No movies available.")
        elif movie_name not in self.movies.values():
            raise ValueError("Movie '{}' doesn't exist".format(movie_name))
        else:
            for rating in self.ratings:
                if rating[1] == movie_name:
                    movie_addition += rating[2]
                    count += 1

            average = movie_addition / count
            print("Calculated average for {} is {}".format(movie_name, average))
            return average

    def get_movies_average_rating(self):
        movie_addition = 0
        count = 0
        if not self.movies:
            raise ValueError("No movies available.")
        else:
            for rating in self.ratings:
                movie_addition += rating[2]
                count += 1

        if count == 0:
            raise ValueError("You cannot divide by zero.")
        average = movie_addition / count
        print("All calculated average is {}".format( average))
        return average