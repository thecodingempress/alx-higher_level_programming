#!/usr/bin/python3
"""
This is a class Square with a private instance attribute and no checks
"""
class Square:
    """
    This is an instance intitialization with a private instance attribute

    Args:
        size (int): private size attribute
    """
    def __init__(self, size):
        self.__size = size
