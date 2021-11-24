#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return

    roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    final = 0
    semi = 0
    for x, y in enumerate(roman_string):
        first = roman[roman_string[x]]
        prev = first
        if x == 0:
            prev = first
        else:
            prev = roman[roman_string[x - 1]]
        if first > prev:
            semi = first - prev - prev
        else:
            semi = first

        final = final + semi

    return final
