#!/usr/bin/python3
import json
"""return a json string"""


def to_json_string(my_obj):
    """coverts daya to json"""
    new_data = json.dumps(my_obj)
    return new_data
