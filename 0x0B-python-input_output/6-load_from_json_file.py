#!/usr/bin/python3
"""module for task 6"""
import json


def load_from_json_file(filename):
    """load object from json file"""
    with open(filename, "r") as f:
        obj = f.read()
        jobj = json.loads(obj)
    return jobj
