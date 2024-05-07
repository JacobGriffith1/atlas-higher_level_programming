#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
i = 10
print(f"Last digit of {number}", end=' ')
if number < 0:
    i = -10
print(f"is {number % i}", end=' ')
if number % i > 5:
    print(f"and is greater than 5")
elif number % i == 0:
    print(f"and is 0")
else:
    print(f"is less than 6 and not 0")
