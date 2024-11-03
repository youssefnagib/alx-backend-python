#!/usr/bin/env python3
"""
Test the utils module
"""


from unittest.mock import Mock, patch
import unittest
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''Test Github'''
    @parameterized.expand([
        ('google,'),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org, mock_get):
        '''Test org'''
        client = GithubOrgClient(org)
        client.org()
        client.org()
        mock_get.assert_called_once_with("https://api.github.com/orgs/" + org)
