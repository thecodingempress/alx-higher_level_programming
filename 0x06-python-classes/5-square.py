#!/usr/bin/python3

"""
class square that takes in the value
and returns or sets it, or the area
"""


class Square:
    """
    initialization of square object with size set to 0

    Args:
        size (int): initialized to 0
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of one side of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        
        self.__size = value

    def area(self):
        """
        returns the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints out the square in teh standard output
        """

        if self.__size == 0:
            print("\n")
        else:
            for i in range(self.__size):
                print('#' * self.__size)
