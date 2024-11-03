#!/usr/bin/env python3
"""
Test the utils module
"""

import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import Mock, patch


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
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''
        test access nested map with exception
        '''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    ''' test get json'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, payload, mock_get):
        '''Test get'''
        mock_response = Mock()
        mock_response.json.return_value = payload

        mock_get.return_value = mock_response

        self.assertEqual(get_json(test_url), payload)


class TestMemoize(unittest.TestCase):
    """Tests the `memoize` function."""
    def test_memoize(self):
        """Tests `memoize`'s output."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as mock:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            mock.assert_called_once()
