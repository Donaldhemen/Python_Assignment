import unittest

from movie_functions import movie_functions


class movie_functions_test(unittest.TestCase):

    def setUp(self):

        self.movie = movie_functions("Inception")

    def test_can_add_movie(self):

        self.assertEqual("Inception", self.movie.get_movie_name())

    def test_movie_has_date_added(self):

        self.assertIsNotNone(self.movie.get_date_added())

    def test_can_add_rating(self):

        self.movie.add_rating(5)

        self.assertEqual(5, self.movie.get_average_rating())

    def test_can_calculate_average_rating(self):

        self.movie.add_rating(5)
        self.movie.add_rating(4)
        self.movie.add_rating(3)

        self.assertEqual(4, self.movie.get_average_rating())

    def test_cannot_add_rating_below_one(self):

        self.movie.add_rating(0)

        self.assertEqual(0, self.movie.get_average_rating())

    def test_cannot_add_rating_above_five(self):

        self.movie.add_rating(6)

        self.assertEqual(0,self.movie.get_average_rating())

    def test_movie_starts_with_zero_ratings(self):

        self.assertEqual(0,self.movie.get_number_of_ratings())


if __name__ == "__main__":
    unittest.main()
