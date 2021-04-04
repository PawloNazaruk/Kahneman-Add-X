import unittest

from assertpy import assert_that

from cls.NumberGame import AddX


class TestNumberGame(unittest.TestCase):

    def setUp(self):
        self.game = AddX()

    def tearDown(self):
        pass

    def test_display_number_with_default_length(self):
        # given
        # when
        result = self.game.display_number()
        # then
        assert_that(result).is_length(4)

    def test_display_number_with_given_length(self):
        # given
        length = 2
        self.game._length = length
        # when
        result = self.game.display_number()
        # then
        assert_that(result).is_length(length)

    def test_display_possible_max_number_with_default_length(self):
        # given
        test_max_number = "9999"
        # when
        result = self.game.display_number()
        # then
        assert_that(result).is_equal_to(test_max_number)


