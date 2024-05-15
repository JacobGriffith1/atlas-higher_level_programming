#!/usr/bin/python3
"""
Unitest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_intrger').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([5, -2, 100, 3], 100))

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)