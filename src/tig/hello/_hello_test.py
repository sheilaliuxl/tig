"""Tests for hello.py"""

from __future__ import absolute_import

import unittest

from tig.hello._hello import hello, add_number, mult_number

class HelloTest(unittest.TestCase):
    """Tests for LinearQubitOperatorOptions class."""

    def test_hello(self):
        """Tests hello()."""
        name = "MyName"
        self.assertEqual(hello(name), "Hello, MyName!")

    def test_add_number(self):
        """Tests add_number()."""
        self.assertEqual(add_number(1, 2), 3)

    def test_mult_number(self):
        """Tests mult_number()."""
        self.assertEqual(mult_number(1, 2), 2)
