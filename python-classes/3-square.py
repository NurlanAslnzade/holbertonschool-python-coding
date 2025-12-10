#!/usr/bin/python3
"""This module defines a Square class"""


class Square:
    """This module defines a Square class"""
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        if not isinstance(self.__size, int):
            raise Exception("size must be an integer")  
        if self.__size < 0:
            raise Exception("size must be >= 0")
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")  
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
