# Unit tests web scraping functions
import unittest
from urllib.error import HTTPError

from src.scraping.scraper import Scraper
from src.scraping.config import headers, zurose_url, zurose_str


class TestScraper(unittest.TestCase):

    def test_instance_no_parameter(self):
        # Check for type error for missing parameter
        with self.assertRaises(TypeError):
            Scraper()

    def test_instance_with_parameter(self):
        scraper = Scraper(header=headers)

# ----- Checking pre-set drugs on drugshortage.ch if they are present or not


# ----- Testing the second part of the Scrapper Class to see if the information from the Zurose webpage is downloaded
    def test_response_status_code_zurose(self):
        scraper = Scraper(header=headers)
        self.assertTrue(scraper.check_response(url=zurose_url) == 200)

    def test_link_to_file_not_found_zurose(self):
        scraper = Scraper(header=headers)
        with self.assertRaises(ValueError):
            scraper.save_file(url=zurose_url, web_button='this is the wrong string')

    def test_link_to_file_correct_zurose(self):
        scraper = Scraper(header=headers)
        file = scraper.save_file(url=zurose_url, web_button=zurose_str)
        self.assertIsNone(file.raise_for_status())


if __name__ == '__main__':
    unittest.main()