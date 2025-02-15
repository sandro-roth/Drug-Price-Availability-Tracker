import unittest

from src.scraping.scraper import Scraper
from src.scraping.config import headers, drug_url

class TestScrapper(unittest.TestCase):

    # Testing the first part of the Scrapper Class
    def setUp(self):
        self.scraper = Scraper(header=headers)

    def test_instance_with_parameter(self):
        self.assertIsInstance(self.scraper, Scraper)

    def test_loading_settings(self):
        parameter = self.scraper.load_yaml()
        self.assertIsInstance(parameter, dict)

    def test_conn_to_web_and_druglist(self):
        list_of_drugs = self.scraper.connect_shortage(drug_url)
        self.assertTrue(isinstance(list_of_drugs, list))


if __name__ == '__main__':
    unittest.main()