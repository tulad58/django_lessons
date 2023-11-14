from unittest import TestCase
from rest_framework.test import APIClient


class TestSomething(TestCase):
    def test_simple(self):
        client = APIClient
        resp = client.get('/api/v1/test/')
        self.assertEqual(resp.status_code, 200)
