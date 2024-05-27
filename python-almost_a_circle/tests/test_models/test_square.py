#!/usr/bin/python3
"""Tests module for class: Square"""
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):
    """Testing suite for class: Square"""