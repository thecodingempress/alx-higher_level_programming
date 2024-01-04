#!/usr/bin/python3
import sys
if __name__ == "__main__":
    number = len(sys.argv) - 1
    if number == 0:
        print("0 arguments.")
    elif number == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(number))

    for index, arg in enumerate(sys.argv[1:], 1):
        print("{}: {}".format(index, arg))
