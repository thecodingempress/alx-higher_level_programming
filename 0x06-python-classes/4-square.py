#!/usr/bin/python3
"""
This class used getters and setters to access and modify the private
attribute age
"""


class Square:
    """
    This initializes the square with a size of 0

    Args: 
        size (int): private attribute size

    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        
        """
        getter for the private attribute size
        setter for size
        """

         return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the area of the square
        
        """
       return self.__size ** 2
