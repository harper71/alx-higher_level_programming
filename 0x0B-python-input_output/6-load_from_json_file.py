#!/usr/bib/python3
"""loads strings from json"""
import json


def load_from_json_file(filename):
    """read from json file

    Args:
        filename (file): filename

    Returns:
        json: loaded data
    """
    with open(filename, 'r') as file:
        data = file.read()
        return json.loads(data)
