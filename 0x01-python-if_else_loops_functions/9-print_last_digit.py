#!/usr/bin/python3
def print_last_digit(number):
    new = 0
    if number < 0:
        new = (-1 * number) % 10
    elif number == 0:
        new = 0
    else:
        new = number % 10
    print("{}".format(new), end="")
    return new
