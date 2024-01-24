#!/usr/bin/python3
"""
This is a class Square with a private instance attribute and no checks
"""
class Square:
    def __init__(self, size):
        """
        This is an instance intitialization with a private instance attribute

        Args:
            size (int): private size attribute
        """
        self.__size = size
