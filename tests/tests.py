import unittest

from assertpy import assert_that

from cls.NumberGame import NumberGame


class TestNumberGame(unittest.TestCase):

    def setUp(self):
        self.client = NumberGame()

    def tearDown(self):
        pass

    def test_game_return_true_when_number_displayed(self):
        # given
        # when
        # then
        assert_that(self.client.game()).is_digit()