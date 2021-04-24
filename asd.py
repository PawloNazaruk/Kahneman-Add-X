import multiprocessing
import time
# from queue import Queue
from collections import deque


def get_kbd_input(result_queue):
    print(f"'get_kbd_input' process started.")
    data = input()
    if data:
        print(f"entry added: {data}")
        result_queue.append(data)
    time.sleep(5)


def count_time(result_queue):
    print(f"'count_time' process started.")
    for i in range(2):
        kbd_input_process = multiprocessing.Process(target=get_kbd_input, args=(result_queue,))
        kbd_input_process.start()
        time.sleep(5)




def main():
    all_processes = []
    result_queue = deque()
    # process = multiprocessing.Process(target=count_time, args=(result_queue,))
    # process.start()
    get_kbd_input_process = multiprocessing.Process(target=get_kbd_input, args=(result_queue,))
    get_kbd_input_process.start()
    time.sleep(3)
    get_kbd_input_process.terminate()
    time.sleep(2)
    print(result_queue)


if __name__ == '__main__':
    main()
