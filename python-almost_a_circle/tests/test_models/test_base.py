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