#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxIntegerFunction(unittest.TestCase):

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element_list(self):
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_positive_numbers(self):
        result = max_integer([1, 3, 2, 8, 5])
        self.assertEqual(result, 8)

    def test_negative_numbers(self):
        result = max_integer([-1, -3, -2, -8, -5])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        result = max_integer([-1, 3, -2, 8, -5])
        self.assertEqual(result, 8)

    def test_duplicate_numbers(self):
        result = max_integer([5, 5, 5, 5])
        self.assertEqual(result, 5)

    def test_float_numbers(self):
        result = max_integer([1.5, 2.5, 0.5])
        self.assertEqual(result, 2.5)

if __name__ == '__main__':
    unittest.main()

