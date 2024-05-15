#!/usr/bin/python3


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """define unittests for max_integer"""

    def test_maxLast(self):
        """max at the end"""
        mlast = [1, 2, 3, 4]
        self.assertEqual(max_integer(mlast), 4)

    def test_maxFirst(self):
        """max at the beginning"""
        mfirst = [4, 1, 2, 3]
        self.assertEqual(max_integer(mfirst), 4)

    def test_maxMid(self):
        """max in the middle"""
        mmid = [1, 2, 5, 3, 4]
        self.assertEqual(max_integer(mmid), 5)

    def test_oneNeg(self):
        """one negative number in the list"""
        oneg = [1, 2, 3, 4, -5]
        self.assertEqual(max_integer(oneg), 4)

    def test_allNeg(self):
        """only negative numbers in the list"""
        aneg = [-4, -3, -2, -1]
        self.assertEqual(max_integer(aneg), -1)

    def test_oneElem(self):
        """list of one element"""
        one = [1]
        self.assertEqual(max_integer(one), 1)

    def test_emptyList(self):
        """list is empty"""
        empty = []
        self.assertEqual(max_integer(empty), None)
