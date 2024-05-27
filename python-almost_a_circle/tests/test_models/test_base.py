#!/usr/bin/python3
"""Tests module for class: Base"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest import TestCase
from unittest.mock import patch


class TestBase(unittest.TestCase):
    """Testing suite for class: Base"""

    def setUp(self):
        """Invoked for each test"""
        Base._Base__nb_objects = 0

    def auto_id(self):
        """Test auto id"""
        new = Base()
        self.assertEqual(new.id, 1)
