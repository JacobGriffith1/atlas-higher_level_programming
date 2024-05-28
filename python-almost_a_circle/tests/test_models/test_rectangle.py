#!/usr/bin/python3
"""Tests module for class: Rectangle"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


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

    def test_three_args(self):
        rec = Rectangle(2, 4, 6)
        rec2 = Rectangle(8, 10, 12)
        self.assertNotEqual(rec.id, rec2.id)

    def test_four_args(self):
        rec = Rectangle(2, 4, 6, 8)
        rec2 = Rectangle(10, 12, 14, 16)
        self.assertNotEqual(rec.id, rec2.id)

    def test_five_args(self):
        rec = Rectangle(2, 4, 6, 8, 10)
        rec2 = Rectangle(12, 14, 16, 18, 20)
        self.assertNotEqual(rec.id, rec2.id)

    def test_six_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 6, 8, 10, 12)

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

    def test_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, "str", 8, 10)

    def test_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 6, "str", 10)

    def test_w_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 10)

    def test_w_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 10)

    def test_w_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({2, 4, 6}, 8)

    def test_w_frozen(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({2, 4, 6, 8}), 10)

    def test_w_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 4)

    def test_w_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 4)

    def test_h_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

    def test_construct(self):
        self.obj = Rectangle(1,1, id=2)
        self.assertEqual(self.obj.height,1)
        self.assertEqual(self.obj.width,1)
        self.assertEqual(self.obj.id, 2)

    def test_strings(self):
        self.obj = Rectangle(2,4,6,8,10)
        self.assertEqual(str(self.obj), "[Rectangle] (10) 6/8 - 2/4")

    def test_area(self):
        rec = Rectangle(3, 5)
        self.assertEqual(rec.area(), 15)

    def test_display(self):
        rec = Rectangle(2, 5)
        dis = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rec.display()
            self.assertEqual(str_out.getvalue(), dis)

    def test_display_2(self):
        rec = Rectangle(2, 2)
        dis = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rec.display()
            self.assertEqual(str_out.getvalue(), dis)

        rec.width = 5
        dis = "#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rec.display()
            self.assertEqual(str_out.getvalue(), dis)

    def test_display_3(self):
        rec = Rectangle(5, 4, 1, 1)
        dis = "\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rec.display()
            self.assertEqual(str_out.getvalue(), dis)

    def test_display_4(self):
        rec = Rectangle(3, 2)
        dis = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rec.display()
            self.assertEqual(str_out.getvalue(), dis)

        rec.x = 4
        dis = "    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rec.display()
            self.assertEqual(str_out.getvalue(), dis)

        rec.y = 2
        dis = "\n\n    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rec.display()
            self.assertEqual(str_out.getvalue(), dis)


if __name__ == '__main__':
    unittest.main()
