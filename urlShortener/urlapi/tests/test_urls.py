from django.test import SimpleTestCase
from django.urls import reverse, resolve

from urlShortener.urlapi import views


class TestUrls(SimpleTestCase):
    """
    Tests verify that correct function is called for specific url
    """
    def test_create_url(self):
        url = reverse('create')
        self.assertEqual(resolve(url).func, views.create_short_url)

    def test_redirect_url(self):
        url = reverse('short')
        self.assertEqual(resolve(url).func, views.short_url_redirect)

    def test_long_url_data(self):
        url = reverse('long_data')
        self.assertEqual(resolve(url).func, views.get_long_url_data)

    def test_short_url_data(self):
        url = reverse('short_data')
        self.assertEqual(resolve(url).func, views.get_short_url_data)
