#!/usr/bin/python3
"""define a class"""
class Square:
    """ define object of the class"""
    def __init__(self, size=0):
        self.__size = size

        """define if size is an integer"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif: size < 0:
            raise ValueError("size must be >= 0")
    
    """define area"""
    def area(self):