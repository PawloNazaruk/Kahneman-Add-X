import unittest

from assertpy import assert_that

from cls.NumberGame import NumberGame


class TestNumberGame(unittest.TestCase):

    def setUp(self):
        self.client = NumberGame(number=6543)

    def tearDown(self):
        pass

    def test_game_return_one_number(self):
        # given
        # when
        # then
        assert_that(self.client.game()).is_digit()

    def test_game_return_one_given_number(self):
        # given
        number = "6543"
        # when
        # then
        assert_that(self.client.game()).is_equal_to(number)
