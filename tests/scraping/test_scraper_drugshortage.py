import unittest

from src.scraping.scraper import Scraper
from src.scraping.config import headers

class TestScrapper(unittest.TestCase):

    # Testing the first part of the Scrapper Class
    def test_instance_no_parameter(self):
        # Check for type error for missing parameter
        with self.assertRaises(TypeError):
            Scraper()

    def test_instance_with_parameter(self):
        scraper = Scraper(header=headers)
        self.assertIsInstance(scraper, Scraper)


if __name__ == '__main__':
    unittest.main()