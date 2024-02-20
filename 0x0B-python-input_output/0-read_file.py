#!/usr/bin/python3

"""
This function reads from a text file and prints
out the content to teh stdandard output
"""


def read_file(filename=""):
    """
    with opens, reads and closes the file
    """

    with open(filename, 'r') as file:
        print(file.read())
