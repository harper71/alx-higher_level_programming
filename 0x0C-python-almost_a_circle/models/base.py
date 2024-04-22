#!/usr/bin/python3
"""class of a base"""
import json
import os


class Base:
    """class called Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts to json string"""
        if list_dictionaries is None or list_dictionaries == "":
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json coverted string to file"""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json_strings = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]
            )
            file.write(json_strings)

    @staticmethod
    def from_json_string(json_string):
        """loads a json file as python string"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates a dummy class

        Returns:
            class: dummy instances
        """
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ loads instances from file"""
        filename = cls.__name__ + ".json"
        with open(filename, "r") as file:
            json_string = file.read()
            dictionaries = cls.from_json_string(json_string)
            dict_1 = cls.create(**dictionary)
            instances = [dict_1 for dictionary in dictionaries]
            return instances
        return []
