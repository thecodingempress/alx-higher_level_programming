#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {} is".format(number), end=" ")

if number < 0:
    new = number % -10
else:
    new = number % 10

if new > 5:
    print("{} and is greater than 5".format(new))
elif new == 0:
    print("{} and is 0".format(new))
elif new < 6 and new != 0:
    print("{} and is less than 6 and not 0".format(new))
