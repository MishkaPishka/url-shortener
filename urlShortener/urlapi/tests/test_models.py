from django.test import TestCase

from urlShortener.urlapi.models import OriginalUrl, ShortUrl, LinkHit
from urlShortener.urlapi.url_queries import get_number_of_different_users_entering_to_long_url, \
    get_number_of_redirects_to_long_url, get_number_of_urls_per_long_url, \
    get_number_of_different_users_clicked_on_short_link


class TestModel(TestCase):
    @classmethod
    def setUpClass(cls):
        # below code will fix AttributeError: type object 'Model Test' has no attribute 'cls_atomics' error.
        super(TestModel, cls).setUpClass()

        # create and save a Department object.
        original_url_name = "http://www.testUrl.com"
        original_url = OriginalUrl(url=original_url_name)
        original_url.save()

        short_url_name = "/s/test"
        short_url = ShortUrl(url=short_url_name, original_url=original_url)
        short_url.save()

        link_hit_source = "localhost"
        short_url = LinkHit(url=short_url, source=link_hit_source)
        short_url.save()

        original_url_name_2 = "http://www.testUrl.com"
        original_url = OriginalUrl(url=original_url_name_2)
        original_url.save()

    def test_distinct_original_url(self):
        original_url = OriginalUrl.objects.update_or_create(url="http://www.testUrl.com")
        self.assertFalse(original_url[1])

    def test_distinct_short_url(self):
        short_url = ShortUrl.objects.update_or_create(url="/s/test")
        self.assertFalse(short_url[1])

    def test_original_link_number_of_hits(self):
        expected_number_of_hits = 1
        actual_number_of_hits = get_number_of_different_users_entering_to_long_url("http://www.testUrl.com")
        self.assertEqual(actual_number_of_hits,expected_number_of_hits)

    def test_number_of_redirects_original_url(self):
        expected_number_of_redirects = 1
        actual_number_of_redirects = get_number_of_redirects_to_long_url("http://www.testUrl.com")
        self.assertEqual(expected_number_of_redirects, actual_number_of_redirects)

    def test_number_of_urls_per_originl_url(self):
        expected_number_of_urls = 1
        actual_number_of_urls = get_number_of_urls_per_long_url("http://www.testUrl.com")
        self.assertEqual(expected_number_of_urls, actual_number_of_urls)

    def test_number_of_different_users_clicked_on_short_url(self):
        expected_number_of_users = 1
        actual_number_of_users = get_number_of_different_users_clicked_on_short_link("http://www.testUrl.com")
        self.assertEqual(expected_number_of_users, actual_number_of_users)

