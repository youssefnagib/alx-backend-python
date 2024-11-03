#!/usr/bin/env python3
"""
Test the utils module
"""


from unittest.mock import Mock, patch, PropertyMock
import unittest
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from typing import Dict
from fixtures import TEST_PAYLOAD
from requests import HTTPError


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


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test"""
    @classmethod
    def setUpClass(cls):
        """Sets up class fixtures before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            '''Get payload'''
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Test public_repos"""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Test public_repos"""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Stop the class fixtures."""
        cls.get_patcher.stop()
