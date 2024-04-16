#!/usr/bin/python3
"""return a json string"""
import json


def to_json_string(my_obj):
    """coverts data to json"""
    new_data = json.dumps(my_obj)
    return new_data
