from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class ServicesURLsTest(TestCase):

    def test_service_index_url_is_correct(self):
        url = reverse('core:services_index')
        self.assertEqual(url, '/')


