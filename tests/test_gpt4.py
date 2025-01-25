# tests/test_gpt4.py

import unittest
from src.gpt4 import GPT4

class TestGPT4(unittest.TestCase):
    def setUp(self):
        """Setup test fixtures, if any."""
        self.gpt4 = GPT4(api_key="fake_api_key", model="gpt-4o-mini")

    def test_prepare_headers(self):
        """Test API headers are set correctly."""
        headers = self.gpt4._prepare_headers()
        self.assertIn('Authorization', headers)
        self.assertEqual(headers['Authorization'], 'Bearer fake_api_key')

    def test_call(self):
        """Test that the call function handles inputs and outputs correctly."""
        # Mocking requests.post to simulate API response
        import requests
        from unittest.mock import patch

        response = {'choices': [{'text': 'test response'}]}
        with patch.object(requests, 'post', return_value=MockResponse(json_data=response)) as mocked_post:
            result = self.gpt4.call("Hello, world!")
            self.assertEqual(result, 'test response')

class MockResponse:
    """Mock requests.Response for testing."""
    def __init__(self, json_data, status_code=200):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.HTTPError(f"{self.status_code}")

if __name__ == '__main__':
    unittest.main()

