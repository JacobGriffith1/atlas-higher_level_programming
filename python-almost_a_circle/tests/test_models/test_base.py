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
