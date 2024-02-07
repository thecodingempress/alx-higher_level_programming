#!/usr/bin/python3
"""
Returns true if object is an instance of a class
inherited from the class
"""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a subclass of a_class, not a_class itself.
    This is achieved by ensuring obj is an instance of a class within the
    inheritance chain of a_class, excluding direct instances of a_class.

    Args:
        obj: object
        a_class: class in question

    Returns:
        True if it is
        False otherwise
    """
    return isinstance(obj, a_class) and not type(obj) is a_class
