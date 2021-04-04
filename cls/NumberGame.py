class AddX:

    def __init__(self, length=4):
        self._length = length

    def display_number(self):
        number_min = 1 * 10**(self._length - 1)
        number_max = int("".join(["9" for x in range(self._length)]))
        number = number_max
        return str(number)

    """
        min_number = 1 * 10**self.length
        max_number = 9 * 10**self.length
        rng = range(min_number, max_number)
        print(rng)
    """