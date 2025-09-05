import unittest
from crawl import normalize_url


class Test_Crawl(unittest.TestCase):
    def test_normalize_url(self):
        input_url = "https://github.com/mdaniyal05"
        actual_url = normalize_url(input_url)
        expected_url = "github.com/mdaniyal05"
        self.assertEqual(actual_url, expected_url)


if __name__ == "__main__":
    unittest.main()
