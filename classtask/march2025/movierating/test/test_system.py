import unittest


from system import System


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.system = System()

    def test_that_system_adds_a_movie_as_dictionary_in_movies(self):
        self.system.add_movie('Movie A')
        self.assertIn('Movie A', self.system.get_movie('Movie A'))
        self.assertIn('Movie A', self.system.get_movie_by_id(1))

    def test_that_system_throws_exception_if_movie_name_was_already_added(self):
        self.system.add_movie('Movie A')
        with self.assertRaises(ValueError):
            self.system.add_movie('Movie A')

    def test_that_movie_can_be_rated(self):
        self.system.add_movie('Movie A')
        self.system.add_movie('Movie B')
        self.system.rate_movie('Movie A', 2)
        self.assertEqual(2, self.system.get_movie_rating('Movie A'))

    def test_that_system_throws_exception_when_movie_name_does_not_exist_during_rate(self):
        self.system.add_movie('Movie A')
        with self.assertRaises(ValueError):
            self.system.rate_movie('Movie B', 2)

    def test_that_system_throws_exception_when_value_name_type_is_not_same_type(self):
        self.system.add_movie('Movie A')
        with self.assertRaises(ValueError):
            self.system.rate_movie('Movie A', 2.5)

    def test_that_movie_average_can_be_gotten(self):
        self.system.add_movie('Movie A')
        self.system.add_movie('Movie B')
        self.system.rate_movie('Movie A', 2)
        self.system.rate_movie('Movie B', 4)
        self.system.rate_movie('Movie A', 4)
        self.assertEqual(4, self.system.get_movie_rating('Movie B'))
        self.assertEqual(2, self.system.get_movie_rating('Movie A'))
        self.assertEqual(3.0, self.system.get_movie_average_rating('Movie A'))
        self.assertEqual(3.3333333333333335, self.system.get_movies_average_rating())

    def test_that_a_movie_average_throws_exception_when_movies_is_empty(self):
        with self.assertRaises(ValueError):
            self.system.get_movie_average_rating('Movie B')

    def test_that_movies_average_throws_exception_when_movies_is_empty(self):
        with self.assertRaises(ValueError):
            self.system.get_movies_average_rating()

    def test_that_a_movie_average_throws_exception_when_movies_name_is_not_found(self):
        self.system.add_movie('Movie A')
        with self.assertRaises(ValueError):
            self.system.get_movie_average_rating('Movie B')

    def test_that_a_movie_average_throws_exception_when_average_is_divided_by_zero(self):
        self.system.add_movie('Movie A')
        with self.assertRaises(ValueError):
            self.system.get_movies_average_rating()


if __name__ == '__main__':
    unittest.main()
