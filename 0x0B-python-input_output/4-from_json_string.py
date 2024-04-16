#!/usr/bin/python3
import json
"""returns a python string"""


def from_json_string(my_str):
    """loads data from json file

    Args:
        my_str (data): json string

    Returns:
        string: loaded data
    """
    new_string = json.loads(my_str)
    return new_string
