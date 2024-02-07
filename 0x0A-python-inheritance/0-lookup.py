#!/usr/bin/python3
"""
function returns a list of attributes
"""


def lookup(obj):
    """the function returns a list of items in an object

    Args:
        obj (object): object in question

    Returns:
        items (list): a list containing the attributes
    """

    items = []
    items = dir(obj)
    return items
