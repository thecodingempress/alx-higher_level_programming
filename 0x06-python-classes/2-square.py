#!/usr/bin/python3
"""
This is a class square that instantiates a private attribute with additional
checks for logic
"""


class Square:
    """
    The class Square intitializes an instance with a private attribute
    and checks the type and value

    Attributes:
        size: private instance that is checked for correct
        type and value
    """

    def __init__(self, size=0):
        """
        This instance initializes an on object with the square size a
        private instance attribute. It check if the size is
        of the correct type and value
        """
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
