#!/usr/bin/env python3
"""
Test the utils module
"""

import unittest
from utils import access_nested_map
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    """
    Test access nested map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''
        test difrrent nested map and path and expected
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        
    ])

if __name__ == '__main__':
    unittest.main()