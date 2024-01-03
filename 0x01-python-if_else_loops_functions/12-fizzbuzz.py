#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            fizzb = "FizzBuzz"
            print("{}".format(fizzb), end=" ")
        elif i % 3 == 0:
            fizz = "Fizz"
            print("{}".format(fizz), end=" ")
        elif i % 5 == 0:
            buzz = "Buzz"
            print("{}".format(buzz), end=" ")
        else:
            print("{}".format(i), end=" ")
