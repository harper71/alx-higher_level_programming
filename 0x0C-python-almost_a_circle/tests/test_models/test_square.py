#!/usr/bin/python3
"""Defines unittests for base.py."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """unittest of square"""
    def test_init(self):
        with self.assertRaises(TypeError):
            square = Square('invalid')
        
        with self.assertRaises(ValueError):
            square = Square(-5)
        
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_update(self):
        square = Square(5)
        with self.assertRaises(TypeError):
            square.update('invalid')

        with self.assertRaises(ValueError):
            square.update(-5)
        
        square.update(1, 10, 2, 3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        
        with self.assertRaises(ValueError):
            square.update(1, -10)

        with self.assertRaises(TypeError):
            square.update(size='invalid')
        
        with self.assertRaises(ValueError):
            square.update(size=-10)

        square.update(size=20, x=5)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 5)

    def test_to_dictionary(self):
        square = Square(5, 2, 3, 1)
        square_dict = {'id': 1, 'width': 5, 'height': 5, 'x': 2, 'y': 3}
        self.assertEqual(square.to_dictionary(), square_dict)

if __name__ == '__main__':
    unittest.main()
