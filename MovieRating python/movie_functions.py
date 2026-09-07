from datetime import datetime


class movie_functions:

    def __init__(self, movie_name):
        self.movie_name = movie_name
        self.date_added = datetime.now()
        self.ratings = []

    def get_movie_name(self):
        return self.movie_name

    def get_date_added(self):
        return self.date_added

    def add_rating(self, rating):

        if rating >= 1 and rating <= 5:
            self.ratings.append(rating)

    def get_average_rating(self):

        if len(self.ratings) == 0:
            return 0

        total = 0

        for rating in self.ratings:
            total += rating

        return total / len(self.ratings)

    def get_number_of_ratings(self):
        return len(self.ratings)
