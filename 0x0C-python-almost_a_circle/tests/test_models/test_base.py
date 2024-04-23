#!/usr/bin/python3
"""Defines unittests for base.py."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """unittests for base"""
    def test_init(self):
        obj1 = Base()
        obj2 = Base()
        obj3 = Base(10)
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 10)

    def test_to_json_string(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")
        
        json_string = Base.to_json_string([{"key": "value"}])
        self.assertEqual(json_string, '[{"key": "value"}]')

    def test_from_json_string(self):
        obj_list = Base.from_json_string("[]")
        self.assertEqual(obj_list, [])
        
        obj_list = Base.from_json_string('[{"key": "value"}]')
        self.assertEqual(obj_list, [{"key": "value"}])

    def test_create(self):
        dictionary = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        obj = Base.create(**dictionary)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 5)
        self.assertEqual(obj.height, 10)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 3)

    def test_load_from_file(self):
        with open("Base.json", "w") as file:
            file.write('[{"id": 1, "width": 5, "height": 10, "x": 2, "y": 3}]')
        
        objs = Base.load_from_file()
        self.assertEqual(len(objs), 1)
        self.assertEqual(objs[0].id, 1)
        self.assertEqual(objs[0].width, 5)
        self.assertEqual(objs[0].height, 10)
        self.assertEqual(objs[0].x, 2)
        self.assertEqual(objs[0].y, 3)

if __name__ == '__main__':
    unittest.main()
