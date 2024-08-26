import random
import time

while True:
    num = random.randint(0, 1)  # Generates a random number that's either 0 or 1

    if num > 0.5:
        print("Heads")
    else:
        print("Tails")
    time.sleep(2)
