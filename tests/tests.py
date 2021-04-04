import unittest

from assertpy import assert_that

from cls.NumberGame import AddX


class TestNumberGame(unittest.TestCase):

    def setUp(self):
        self.game = AddX()

    def tearDown(self):
        pass

    def test_display_number_with_four_length(self):
        # given
        number = "3333"
        # when
        # then
        assert_that(self.game.display_number()).is_equal_to(number)
