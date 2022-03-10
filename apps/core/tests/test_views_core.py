from django.test import TestCase
from django.urls import reverse, resolve
from django.test import Client

# Create your tests here.

class CoreViewsTest(TestCase):
    def test_core_login_user_is_correct(self):
        view = resolve(reverse('core:login'))
        self.assertIs(view)