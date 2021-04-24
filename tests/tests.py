import unittest
import time
from datetime import datetime

from assertpy import assert_that

from cls.NumberGame import GameAddX


class TestNumberGame(unittest.TestCase):

    def setUp(self):
        default_kwargs = {
            "length": "4",
            "amount": "5",
            "time_for_number": "1",
            "time_for_pause": "1",
            "operation": "+",
            "digit_for_operation": "1",
        }
        self.game = GameAddX(**default_kwargs)

    def tearDown(self):
        pass

    @unittest.skip()
    def test_display_number_with_default_length(self):
        # given
        # when
        result = self.game.display_numbers()
        # then
        assert_that(result).is_length(4)

    @unittest.skip()
    def test_display_number_with_given_length(self):
        # given
        length = 2
        self.game = AddX(length=2, amount=1)
        # when
        result = self.game.display_numbers()
        # then
        assert_that(result).is_length(length)

    @unittest.skip('nothing to do here')
    def test_display_possible_max_number_with_default_length(self):
        """# given
        test_max_number = "9999"
        # when
        result = self.game.display_number()
        # then
        assert_that(result).is_equal_to(test_max_number)"""
        pass

    @unittest.skip()
    def test_display_random_number_with_default_length(self):
        # given
        minimum = 1000
        maximum = 9999
        # when
        result = self.game.display_numbers()
        result = int(result)
        # then
        assert_that(result).is_between(minimum, maximum)

    @unittest.skip()
    def test_display_five_random_numbers_with_default_length(self):
        # given
        pattern = r"^\d{4}\n\d{4}\n\d{4}\n\d{4}\n\d{4}$"
        kwargs = {"length": 4, "amount": 5}
        self.game = AddX(**kwargs)
        # when
        result = self.game.display_numbers()
        print(result)
        # then
        assert_that(result).matches(pattern)

    @unittest.skip()
    def test_display_number_with_default_wait_time(self):
        # given
        self.game = AddX(length=4, amount=1, wait=3)
        # when
        start_time = datetime.now()
        self.game.display_number()
        end_time = datetime.now()
        # then
        print(start_time)
        print(end_time)
        print((end_time - start_time).total_seconds())
