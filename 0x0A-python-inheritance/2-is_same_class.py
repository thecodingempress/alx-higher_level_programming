#!/usr/bin/python3

"""
Function returns true if object is excatlu and instance
of teh specified class, otherwise false
"""


def is_same_class(obj, a_class):
    """ checks with isinstance
    Args:
        obj: onject in question
        a_class: class

    Returns:
        True if object is an instance of the class
        False if not
    """

    if type(obj) is (a_class):
        return True
    else:
        return False
