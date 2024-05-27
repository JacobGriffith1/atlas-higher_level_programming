#!/usr/bin/python3
"""Tests module for class: Base"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """Testing suite for class: Base"""

    def test_None(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_Empty(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_single_id(self):
        self.assertEqual(5, Base(5).id)

    def test_public_id(self):
        public = Base(5)
        public.id = 10
        self.assertEqual(10, public.id)

    def test_private_ins(self):
        with self.assertRaises(AttributeError):
            print(Base(5).__nb_instances)

    def test_str(self):
        self.assertEqual("string", Base("string").id)

    def test_float(self):
        self.assertEqual(3.14, Base(3.14).id)

    def test_list(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_dict(self):
        self.assertEqual({"funnynum1": 69, "funnynum2": 420}, Base({"funnynum1": 69, "funnynum2": 420}).id)

    def test_tuple(self):
        self.assertEqual((1, 2, 3), Base((1, 2, 3)).id)

class TestToJson(unittest.TestCase):
    """Testing suite for method: to_json_string"""

    def test_to_json_none(self):
        self.assertEqual('[]', Base.to_json_string(None))

    def test_to_json_empty(self):
        self.assertEqual('[]', Base.to_json_string([]))

    def test_to_json_TypeError(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_TypeError2(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 21)

class TestFromJson(unittest.TestCase):
    """Testing suite for methon: from_json_string"""

    def test_from_json_none(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_empty(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_TypeError(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_TypeError2(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 789)
