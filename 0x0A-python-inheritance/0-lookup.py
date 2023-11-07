#!/usr/bin/python3
"""
Contains the lookup function
"""


def lookup(obj):
    """returns a list of available attributes and method of an object"""
    return dir(obj)
