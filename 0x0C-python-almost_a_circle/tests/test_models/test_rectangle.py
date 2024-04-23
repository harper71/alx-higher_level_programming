#!/usr/bin/python3
"""Defines unittests for rectanglee.py."""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """unittest for rectangle"""
    def test_init(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle('invalid', 10, 2, 3, 1)
        
        with self.assertRaises(ValueError):
            rectangle = Rectangle(-5, 10, 2, 3, 1)

        rectangle = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.id, 1)

    def test_area(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)

    def test_display(self):
        # Not testing output here, just checking if method executes without error
        rectangle = Rectangle(5, 10)
        rectangle.display()

    def test_to_dictionary(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        rectangle_dict = {'_Rectangle__height': 10, '_Rectangle__width': 5, '_Rectangle__x': 2, '_Rectangle__y': 3, 'id': 1}
        self.assertEqual(rectangle.to_dictionary(), rectangle_dict)

    def test_update(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        
        with self.assertRaises(TypeError):
            rectangle.update('invalid')
        
        with self.assertRaises(ValueError):
            rectangle.update(-5, 10, 2, 3, 1)

        rectangle.update(2, 20, 15, 4, 5)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 20)
        self.assertEqual(rectangle.height, 15)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 5)
        
        rectangle.update(width=25, height=30)
        self.assertEqual(rectangle.width, 25)
        self.assertEqual(rectangle.height, 30)

if __name__ == '__main__':
    unittest.main()
