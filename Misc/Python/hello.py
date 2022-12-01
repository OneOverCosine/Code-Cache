import sys
import time
from my_array import my_array


def timed_count(counter):
    for i in range(counter):
        print(i, end = ' ')
        sys.stdout.flush()
        time.sleep(1)


if __name__ == "__main__":
    
    numbers = my_array(3)
    numbers.print_array()

    input('\nPress enter to exit\n')