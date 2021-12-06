#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    highest = 0
    who = ""
    for name, score in a_dictionary.items():
        if score > highest:
            highest = score
            who = name
    return who
