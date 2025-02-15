import unittest

from src.scraping.scraper import Scraper
from src.scraping.config import headers, zurose_url, zurose_str


class TestScraper(unittest.TestCase):

    # Testing the second part of the Scrapper Class to see if the information from the Zurose webpage is downloaded
    def setUp(self):
        self.scraper = Scraper(header=headers)

    def test_response_status_code_zurose(self):
        self.assertTrue(self.scraper.check_response(url=zurose_url) == 200)

    def test_link_to_file_not_found_zurose(self):
        with self.assertRaises(ValueError):
            self.scraper.save_file(url=zurose_url, web_button='this is the wrong string')

    def test_link_to_file_correct_zurose(self):
        file = self.scraper.save_file(url=zurose_url, web_button=zurose_str)
        self.assertIsNone(file.raise_for_status())


if __name__ == '__main__':
    unittest.main()