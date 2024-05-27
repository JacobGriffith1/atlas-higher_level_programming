#!/usr/bin/python3
"""Tests module for class: Rectangle"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Testing suite for class: Rectangle"""

    def test_isRec(self):
        self.assertIsInstance(Rectangle(3, 5), Base)

    def test_empty(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_width_priv(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 4, 6, 8, 10).__width)
    
    def test_width_getter(self):
        rec = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual(2, rec.width)

    def test_width_setter(self):
        rec = Rectangle(2, 4, 6, 8, 10)
        rec.width = 2
        self.assertEqual(2, rec.width)
