"""Tests for hello.py"""

from __future__ import absolute_import

import unittest

from tig.hello._hello import hello, add_number
# from openfermion.utils._sparse_tools import qubit_operator_sparse

class HelloTest(unittest.TestCase):
    """Tests for LinearQubitOperatorOptions class."""

    def test_hello(self):
        """Tests hello()."""
        name = "MyName"
        self.assertEqual(hello(name), "Hello, MyName!")

    def test_add_number(self):
        """Tests add_number()."""
        self.assertEqual(add_number(1, 2), 3)
