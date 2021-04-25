from collections import namedtuple
from threading import Thread
from pprint import pprint
import random
import time


class GameAddX:

    def __init__(self, length: str, amount: str, time_for_number: str, time_for_pause: str, operation: str, digit_for_operation: str):
        self._number_length = int(length)
        self._numbers_amount = int(amount)
        self._time_per_number = int(time_for_number)
        self._time_per_pause = int(time_for_pause)
        self._math_operation = operation
        self._math_operation_sign = int(digit_for_operation)
        self._game_session = self.make_game_session()
        self._input = []

    def game(self):
        for seq in self._game_session:
            pprint(self._game_session)

            """displaying digits for memorise"""
            for digit in seq.number_digits:
                print(digit)
                self.wait_number()

            """pause"""
            self.wait_pause()

            """catching answers"""
            for i in range(self._number_length):
                get_input_thread = Thread(target=self.get_input)
                get_input_thread.daemon = True  # Otherwise the thread won't be terminated when the main program terminates.
                get_input_thread.start()
                get_input_thread.join(timeout=3)

                seq.answer_digits.append(self._input[0])
                self._input.clear()
        print(self._game_session)

    def get_input(self):
        print("Waiting for input: ...")
        while True:
            _input = input()
            self._input.append(_input)

    def wait_number(self) -> None:
        time.sleep(self._time_per_number)

    def wait_pause(self) -> None:
        time.sleep(self._time_per_pause)

    def make_game_session(self):
        Sequence = namedtuple("Sequence", [
            "number_digits",
            "correct_digits",
            "answer_digits",
        ])

        number = self.generate_number_from_range()
        number_digits = self.divide_on_digits(number)
        correct_digits = self.generate_answer_number_digits(number)
        answer_digits = []

        seq = Sequence(number_digits, correct_digits, answer_digits)
        return [seq for _ in range(self._numbers_amount)]

    def generate_number_from_range(self) -> str:
        number_min = 10 ** (self._number_length - 1)
        number_max = int("".join(["9" for _ in range(self._number_length)]))
        return str(random.randint(number_min, number_max))

    @staticmethod
    def divide_on_digits(number: str) -> list:
        return [x for x in number]

    def generate_answer_number_digits(self, number: str) -> list:
        return {
            "+": [str(int(x) + self._math_operation_sign) for x in number],
            "-": [str(int(x) - self._math_operation_sign) for x in number],
            "*": [str(int(x) * self._math_operation_sign) for x in number],
            "/": [str(int(x) / self._math_operation_sign) for x in number],
        }.get(self._math_operation, "Incorrect operation")


# property na limity
default_kwargs = {
            "length": 3,
            "amount": 1,
            "time_for_number": 1,
            "time_for_pause": 1,
            "operation": "+",
            "digit_for_operation": 1,
        }
asd = GameAddX(**default_kwargs)
asd.game()
