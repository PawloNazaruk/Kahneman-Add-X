from threading import Thread
import time


class myClass:
    _input = None

    def __init__(self):

        for i in range(5):
            get_input_thread = Thread(target=self.get_input)
            get_input_thread.daemon = True  # Otherwise the thread won't be terminated when the main program terminates.
            get_input_thread.start()
            get_input_thread.join(timeout=5)

            if myClass._input is None:
                print("No input was given within 5 seconds")
            else:
                print("Input given was: {}".format(myClass._input))

    @classmethod
    def get_input(cls):
        print("Wainting for input: ...")
        cls._input = input()
        time.sleep(5)

obj = myClass()

