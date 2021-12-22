#!/usr/bin/python3
"""module for task 4"""
import json


def from_json_string(my_str):
    """get python object from json"""
    return json.loads(my_str)
