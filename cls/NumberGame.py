import random


class AddX:

    def __init__(self, length=4):
        self._length = length

    def display_number(self):
        number_min = 10**(self._length - 1)
        number_max = int("".join(["9" for x in range(self._length)]))
        number = random.randint(number_min, number_max)
        return str(number)
