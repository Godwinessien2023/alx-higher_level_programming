#!/usr/bin/python3
"""Define and object attribut look up function"""


def lookup(obj):
    """return the list of an objects available attributes"""
    return (dir(obj))
