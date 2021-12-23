#!/usr/bin/python3
"""module for Student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """class constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        my_dict = {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age,
                }

        if attrs is None:
            return my_dict
        new_dict = {}
        for item in attrs:
            if item in ['first_name', 'last_name', 'age']:
                new_dict[item] = my_dict[item]
        return new_dict

    def reload_from_json(self, json):
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
