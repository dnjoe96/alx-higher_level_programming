#!/usr/bin/python3
"""module for Student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """class constructor"""
        self.fname = first_name
        self.lname = last_name
        self.age = age

    def to_json(self):
        my_dict = {}
        my_dict['first_name'] = self.fname
        my_dict['last_name'] = self.lname
        my_dict['age'] = self.age
        return my_dict
