#!/usr/bin/python3
"""Doc"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Doc"""
    def test_no_argument(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.idm - 1)

    def test_three_object(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, base2.id - 2)
    
    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

