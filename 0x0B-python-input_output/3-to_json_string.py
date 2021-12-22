#!/usr/bin/python3
""" module for task 3"""
import json

def to_json_string(my_obj):
    """transform object to json"""
    jobj = json.dumps(my_obj)
    return jobj
