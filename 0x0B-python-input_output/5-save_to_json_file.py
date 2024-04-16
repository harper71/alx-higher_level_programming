#!/usr/bin/python3
"""write a string to a json file"""
import json


def save_to_json_file(my_obj, filename):
    """encoders to json

    Args:
        my_obj (object): obk=ject to encode
        filename (file): filename
    """
    with open(filename, 'w') as Jfile:
        data = json.dump(my_obj, Jfile)
