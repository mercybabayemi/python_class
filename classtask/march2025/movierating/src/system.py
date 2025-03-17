from datetime import datetime

class System:
    def __init__(self):
        self.movies = {}
        self.movie_count = 1
        self.ratings = []

    def add_movie(self, name):
        if any(movie['title'] == name for movie in self.movies.values()):
            raise ValueError("'{}' already exists".format(name))

        each_name = "movie" + str(self.movie_count)
        self.movies[each_name] = {
            'title': name,
            'date': datetime.now()
        }
        self.movie_count += 1
        print("Movie added successfully")

    def get_movie(self, name):
        for movie in self.movies.values():
            if movie['title'] == name:
                return movie
        return "Movie '{}' doesn't exist".format(name)

    # def get_movie_by_id(self, value):
    #     if value not in self.movies:
    #         return f"Movie with index {value} doesn't exist"
    #     else:
    #         return self.movies[value]

    def rate_movie(self, movie_name, value):
        movie = self.get_movie(movie_name)
        if isinstance(movie, str):
            raise ValueError(movie)

        if type(value) is not int:
            raise ValueError("'{}' value is not an integer".format(value))

        self.ratings.append([movie_name, value])
        print("Movie '{}' has been rated successfully".format(movie_name))

    def get_movie_rating(self, movie_name):
        for rating in self.ratings:
            if rating[0] == movie_name:
                return rating[1]
        return "No rating for '{}'".format(movie_name)

    def view_available_movies(self):
        if not self.movies:
            print("No movies available.")
        else:
            print("Available movies:")
            for movie in self.movies.values():
                print(f"{movie['title']} is created by {movie['date']}")

    def get_movie_average_rating(self, movie_name):
        movie_addition = 0
        count = 0
        if not self.movies:
            raise ValueError("No movies available.")
        else:
            for rating in self.ratings:
                if rating[0] == movie_name:
                    movie_addition += rating[1]
                    count += 1

            if count == 0:
                raise ValueError("No ratings for '{}'".format(movie_name))

            average = movie_addition / count
            print("Calculated average for {} is {}".format(movie_name, round(average, 2)))
            return round(average, 2)

    def get_movies_average_rating(self):
        movie_addition = 0
        count = 0
        if not self.movies:
            raise ValueError("No movies available.")
        else:
            for rating in self.ratings:
                movie_addition += rating[1]
                count += 1

        if count == 0:
            raise ValueError("Please rate at least one movie.")
        average = movie_addition / count
        print("All calculated average is {}".format(round(average, 2)))
        return round(average, 2)