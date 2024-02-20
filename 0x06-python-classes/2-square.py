#!/usr/bin/python3

""" This is a class for a swuare"""


class Square:

    """This tim with an objecy attribute"""
    def __init__(self, size=0):
        """ initialixes a class attribute"""
        self.size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError(size must be >= 0)
