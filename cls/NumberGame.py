import random
import time
from collections import namedtuple
from pprint import pprint


class GameAddX:

    def __init__(self, length: str, amount: str, time_for_number: str, time_for_pause: str, operation: str, digit_for_operation: str):
        self._length = int(length)
        self._amount = int(amount)
        self._time_for_number = int(time_for_number)
        self._time_for_pause = int(time_for_pause)
        self._operation = operation
        self._digit_for_operation = int(digit_for_operation)  # any better name??
        self._numbers = self.prepare_game()

    def game(self):
        for pair in self._numbers:
            # displaying digits for memorise
            for digit in pair.number_digits:
                self.display_digit(digit)
            # pause
            self.display_pause()
            # digits given by the user after the action
            # @2 Gather input without stopping time
            for digit in pair.correct_digits:

                start = time.time()
                stop = time.time()
                delta = stop - start
                user_input = ""
                print("start")
                print(delta)
                while delta <= self._time_for_number:
                    #user_input = input()
                    pair.answer_digits.append(user_input)
                    delta = time.time() - start
                print("end")
                print(delta)

    def display_digit(self, digit: str) -> None:
        print(digit)
        time.sleep(self._time_for_number)

    def display_pause(self) -> None:
        print("")
        time.sleep(self._time_for_pause)

    def prepare_game(self):
        Pair = namedtuple("Pair", [
            "number_digits",
            "correct_digits",
            "answer_digits",
        ])
        number = self.generate_number()
        digits = self.generate_number_digits(number)
        correct_digits = self.generate_answer_number_digits(number)
        answer_digits = []
        pair = Pair(digits, correct_digits, answer_digits)
        return [pair for _ in range(self._amount)]

    def generate_number(self) -> str:
        number_min = 10 ** (self._length - 1)
        number_max = int("".join(["9" for _ in range(self._length)]))
        number = random.randint(number_min, number_max)
        return str(number)

    @staticmethod
    def generate_number_digits(number: str) -> list:
        return [str(x) for x in number]

    def generate_answer_number_digits(self, number: str) -> list:
        return {
            "+": [str(int(x) + self._digit_for_operation) for x in number],
            "-": [str(int(x) - self._digit_for_operation) for x in number],
            "*": [str(int(x) * self._digit_for_operation) for x in number],
            "/": [str(int(x) / self._digit_for_operation) for x in number],
        }.get(self._operation, "Incorrect operation")


# property na limity
default_kwargs = {
            "length": 4,
            "amount": 1,
            "time_for_number": 1,
            "time_for_pause": 1,
            "operation": "+",
            "digit_for_operation": 1,
        }
asd = GameAddX(**default_kwargs)
print(asd._operation)
print(asd.generate_number())
pprint(asd.prepare_game())
asd.game()