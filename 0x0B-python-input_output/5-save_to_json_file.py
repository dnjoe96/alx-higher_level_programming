#!/usr/bin/python3
"""module for task 5"""
import json


def save_to_json_file(my_obj, filename):
    """save to json file"""
    with open(filename, "w") as f:
        jobj = json.dumps(my_obj)
        num = f.write(jobj)
    return num
