#!/usr/bin/python3
def add_integer(a, b=98):
    
    """check if a is an interger or float otherwise, raise typeerror"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    """check if b is an integer or float otherwise, raise a TypeError"""
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or b must be an integer")

    return (int(a) + int(b))
