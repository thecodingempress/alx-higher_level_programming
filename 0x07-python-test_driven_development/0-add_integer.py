#!/usr/bin/python3

"""
Function adds two integers while using unit tests
"""


def add_integer(a, b = 98):
    if  not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float))::
        raise TypeError("b must be an integer")

    a = int(a) 
    b = int(b)

    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/add_integer.txt")
