import unittest

from src.scraping.scraper import Scraper
from src.scraping.config import headers, drug_url

class TestScrapper(unittest.TestCase):

    # Testing the first part of the Scrapper Class
    def test_instance_no_parameter(self):
        # Check for type error for missing parameter
        with self.assertRaises(TypeError):
            Scraper()

    def test_instance_with_parameter(self):
        scraper = Scraper(header=headers)
        self.assertIsInstance(scraper, Scraper)

    def test_loading_settings(self):
        scraper = Scraper(header=headers)
        parameter = scraper.load_yaml()
        self.assertIsInstance(parameter, dict)

    def test_conn_to_web_and_druglist(self):
        scraper = Scraper(header=headers)
        list_of_drugs = scraper.connect_shortage(drug_url)
        self.assertTrue(isinstance(list_of_drugs, list))


if __name__ == '__main__':
    unittest.main()