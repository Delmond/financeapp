from django.test import TestCase
from news.utils import get_url, filter_fields
from urllib.parse import urlparse
from collections import namedtuple
from time import localtime
# Create your tests here.


class UtilMethodsTestCase(TestCase):

    def test_url_contains_symbol_query_param(self):
        url = get_url("AAPL")
        parsed_url = urlparse(url)
        self.assertIn("s=AAPL", parsed_url.query)

    def test_url_has_correct_base(self):
        url = get_url("AAPL")
        parsed_url = urlparse(url)
        self.assertEqual('feeds.finance.yahoo.com', parsed_url.netloc)

    def test_filter_fields_gets_correct_fields(self):
        mock = namedtuple("mocked_response", "id title summary published_parsed link")
        data = mock("55bf83ec-cc2d-31ee-8d63-93114a91cbbd", "some title", "some summary", localtime(), "https://example.com")
        filtered = filter_fields(data)

        self.assertEqual(filtered['title'], data.title)
        self.assertEqual(filtered['description'], data.summary)
        self.assertEqual(filtered['link'], data.link)