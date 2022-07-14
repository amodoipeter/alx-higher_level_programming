#!/usr/bin/python3
"""Test Rectangle"""
import unittest
import pep8
from models.base import Base
from models.base import Rectangle


class Testrectangle(unittest.TestCase):
    """ """

    def test_pep8_conformance_rectangle(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_subclass(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_parameters(self):
        """ """
        r1 = Rectangle()
        r2 = Rectangle()
        r3 = Rectangle()
        self.assertEqual(r1.id, 4)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.id, 5)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        with self.assertRaises(TypeError):
            Rectangle()

    def test_string(self):
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle()

    def test_type_param(self):
        with self.assertRaises(TypeError):
            Rectangle()
            raise TypeError()
        with self.assertRaises(ValueError):
            Rectangle()
            raise ValueError()
        with self.assertRaises(TypeError):
            Rectangle()
            raise TypeError()
        with self.assertRaises(TypeError):
            Rectangle()
            raise TypeError()
        with self.assertRaises(TypeError):
            Rectangle()
            raise TypeError()
        with self.assertRaises(TypeError):
            Rectangle()
            raise TypeError()
        with self.assertRaises(TypeError):
            Rectangle()
            raise TypeError()
        with self.assertRaises(ValueError):
            Rectangle()
            raise ValueError
        with self.assertRaises(TypeError):
            Rectangle()
            raise TypeError()
        with self.assertRaises(TypeError):
            Rectangle()
            raise TypeError()
        with self.assertRaises(TypeError):
            Rectangle()
            raise TypeError()
        with self.assertRaises(ValueError):
            Rectangle()
            raise ValueError()
        with self.assertRaises(TypeError):
            Rectangle()
            raise TypeError()
        with self.assertRaises(TypeError):
            Rectangle()
            raise TypeError()
        with self.assertRaises(TypeError):
            Rectangle()
            raise TypeError()
        with self.assertRaises(ValueError):
            Rectangle()
            raise ValueError()
