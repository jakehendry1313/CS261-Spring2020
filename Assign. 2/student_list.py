# Author:      Jacob Hendry
# Date:        04/21/2020
# Description: This is a python file called student_list.py. It will be an
#              a reimplementation of Pythons List.

import numpy as np


# StudentList class is our implementation of Python's List
class StudentList:
    def __init__(self):
        # creates an empty array of length 4, change the [4] to another value to make an
        # array of different length.
        self._list = np.empty([4], np.int16)
        self._capacity = 4
        self._size = 0

    def __str__(self):
        return str(self._list[:self._size])

    def get_list(self):
        return self._list[:self._size]

    def get_capacity(self):
        return self._capacity

    def append(self, val):
        """Adds a value to the end of the list of the array"""
        if self._size >= self._capacity:
            self.resize_array()
        self._list[self._size] = val
        self._size = self._size + 1

    def resize_array(self):
        """Doubles the size of the array"""
        new_list = np.empty([self._capacity * 2], np.int16)
        for x in range(len(self._list)):
            new_list[x] = self._list[x]
        self._list = new_list
        self._capacity = self._capacity * 2

    def pop(self):
        """Removes the last value in the array"""
        if self._size == 0:
            print("List is empty")
            return
        else:
            self._size = self._size - 1
            return self._list[self._size]

    def insert(self, index, val):
        """Insert a value in a specific index"""
        if self._size >= self._capacity:
            self.resize_array()
        self._list = np.insert(self._list, index, val)
        self._size = self._size + 1

    def remove(self, val):
        """Remove a value from the array"""
        if self._size == 0:
            print("There are no values to remove")
        elif val in self._list:
            self._list = np.delete(self._list, np.where(self._list == val))
            self._size = self._size - 1
        else:
            print("Value doesn't exist")

    def clear(self):
        """Clear the entire array"""
        self.remove(self._list)

    def count(self, val):
        """Returns the number of times the value is in the array"""
        counter = 0
        for x in self._list:
            if val == x:
                counter = counter + 1
        return counter

    def get(self, index):
        """Get the value from the array"""
        if index < self._size:
            return self._list[index]
        else:
            print("Index doesn't exist")

