import unittest
from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class TestCoreView(TestCase):

    def test_core_index_url_is_correct(self):
        url = reverse('core:core_index')
        self.assertEqual(url,'/')

    def test_core_login_url_is_correct(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_core_logout_url_is_correct(self):
        response = self.client.get('logout/')
        self.assertEqual(response.status_code, 404)


