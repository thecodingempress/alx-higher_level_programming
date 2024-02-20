#!/usr/bin/python3

"""

"""


class Square:
    """

    """
    def __init__(self, position = (0,0), size = 0):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        self.__size = value

    @property
    def position (self):
        return self.__position

    @position.setter
    def position (self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of two positive integers")
        self.__position = value


    def area(self):
        return self.__size **2

    def my_print(self):
        if self.__size == 0:
            print("")
            return

            for i in range(self.__position[1]):
                print("")

            for k in range(self.__size):
                print(" " * self.position[0] + '#' * self.__size)
