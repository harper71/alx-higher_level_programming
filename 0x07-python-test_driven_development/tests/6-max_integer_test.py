#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        #checks for the maximum max integer
        self.assertAlmostEquals(max_integer([1, 2, 3, 4]), 4)
    def test_values(self):
        self.assertRaises(TypeError, max_integer, ["add", "willam", "wrw32"])
        self.assertRaises(TypeError, max_integer, [1.3, 4.5, 46.4])
        self.assertRaises(IndexError, max_integer, [])
