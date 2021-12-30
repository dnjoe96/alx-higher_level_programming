#!/usr/bin/python3
"""module for Student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """class constructor"""
        self.fname = first_name
        self.lname = last_name
        self.age = age

    def to_json(self, attrs=None):
        my_dict = {
                'first_name': self.fname,
                'last_name': self.lname,
                'age': self.age,
                }

        if attrs is None:
            return my_dict
        new_dict = {}
        for item in attrs:
            if item in ['first_name', 'last_name', 'age']:
                new_dict[item] = my_dict[item]
        return new_dict
