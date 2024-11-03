#!/usr/bin/env python3
"""
Test the utils module
"""


from unittest.mock import Mock, patch, PropertyMock
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict


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

    def test_public_repos_url(self):
        '''Test public'''
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            # make it return a known payload.
            mock.return_value = {"repos_url": "google"}
            client = GithubOrgClient("...")
            self.assertEqual(client._public_repos_url, "google")

    @patch('client.get_json')
    def test_public_repos(self, mock_get):
        '''Test public repositories.'''
        mock_get.return_value = {"repos_url": "google"}
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            # make it return a known payload.
            mock.return_value = {"repos_url": "google"}
            client = GithubOrgClient("...")
            self.assertEqual(client._public_repos_url, "google")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict[str, Dict], license_key: str,
                         expected_returned: bool):
        '''Check that the given license'''
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected_returned)
