#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_value = None
    best_key = None
    for key, values in a_dictionary.items():
        if max_value is None or values > max_value:
                max_value = values
                best_key = key
    return max_value
