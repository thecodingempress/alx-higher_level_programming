#!/usr/bin/python3
"""
Returns true if object is an instance of or instance if a class
inherited from the class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is instance of class or inherited class

    Args:
        obj: object
        a_class: class in question

    Returns:
        True if it is
        False otherwise
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
