#!/usr/bin/python3
"""module for task 7"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

dfile = "add_item.json"

try:
    with open(dfile, 'r') as f:
        num = len(f.read())
except FileNotFoundError:
    f = open(dfile, 'w')
    f.close()
    num = 0

if num == 0:
    dlist = []
else:
    obj = load_from_json_file(dfile)
    dlist = obj

dlist = dlist + sys.argv[1:]

save_to_json_file(dlist, dfile)
