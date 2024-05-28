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

    def test_height_priv(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 4, 6, 8, 10).__height)

    def test_height_getter(self):
        rec = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual(4, rec.height)

    def test_height_setter(self):
        rec = Rectangle(2, 4, 6, 8, 10)
        rec.height = 4
        self.assertEqual(4, rec.height)

    def test_x_priv(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 4, 6, 8, 10).__x)

    def test_x_getter(self):
        rec = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual(6, rec.x)

    def test_x_setter(self):
        rec = Rectangle(2, 4, 6, 8, 10)
        rec.x = 10
        self.assertEqual(10, rec.x)

    def test_y_priv(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 4, 6, 8, 10).__y)

    def test_y_getter(self):
        rec = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual(8, rec.y)

    def test_y_setter(self):
        rec = Rectangle(2, 4, 6, 8, 10)
        rec.y = 10
        self.assertEqual(10, rec.y)

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(2)

    def test_two_args(self):
        rec = Rectangle(2, 4)
        rec2 = Rectangle(6, 8)
        self.assertNotEqual(rec.id, rec2.id)

    def test_w_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_w_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("string", 2)

    def test_h_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "string")

    def test_w_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(3.14, 2)

    def test_h_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 3.14)

    def test_w_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"str": 18, "int": 8}, 2)

    def test_w_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([2, 4, 6], 8)

    def test_w_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((2, 4, 6), 8)


if __name__ == '__main__':
    unittest.main()
