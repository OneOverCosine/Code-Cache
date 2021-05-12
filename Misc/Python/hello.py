import sys
import time

# seemed a suitable way to start off this repo
# print("Hello world!")
for i in range(10):
    print(i, end = ' ')
    sys.stdout.flush()
    time.sleep(1)

input('\nPress enter to exit\n')