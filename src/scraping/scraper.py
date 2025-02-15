# Main scraping script
import requests
from bs4 import BeautifulSoup
import os

from utils import YamlHandler
from src.scraping.config import headers, drug_url

class Scraper:
    parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    data_dir = os.path.join(parent_dir, 'data', 'raw')
    yml_path = os.path.join(parent_dir, 'config', 'settings.yml')

    def __init__(self, header):
        self.header = header

    def check_response(self, url):
        self.resp = requests.get(url=url, headers=self.header, timeout=1)
        return self.resp.status_code

    def load_yaml(self):
        yml = YamlHandler()
        parameter = yml.loader(self.yml_path)
        return parameter

    def connect_shortage(self, url):
        assert self.check_response(url) == 200
        assert isinstance(self.load_yaml()['druglist'], list)
        return self.load_yaml()['druglist']

    def parse_shortage(self, url):
        # include first part in try statement till for loop
        # druglist = self.connect_shortage(url)
        # soup = BeatuifulSoup(self.resp.text, 'html.parser')
        # for loop through list of drugs
        # find drugname in Bezeichnung # use if else statement to check if present (not sure
        # get first file from the link and save it in raw_data
        # name it with bezeichnung.csv
        # do the last two for all
        pass

    def save_file(self, url, web_button):
        """Get the .xlsx file from zu rose homepage"""
        assert self.check_response(url) == 200
        soup = BeautifulSoup(self.resp.text, 'html.parser')
        link = soup.find('a', string=web_button)
        if not link:
            raise ValueError('The button to download the file changed')

        file_url = link['href']
        if not file_url.startswith('http'):
            file_url = requests.compat.urljoin(url, file_url)

        # Download the file
        file_response = requests.get(file_url)

        # Save the file
        file = 'non_deliverable_items_list.xlsx'
        xlsx_filename = os.path.join(self.data_dir, file)
        with open(xlsx_filename, 'wb') as file:
            for chunk in file_response.iter_content(chunk_size=128):
                file.write(chunk)

        return file_response





# Check the swica drug directory for information on manufacturers and prices


if __name__ == '__main__':
    scrap = Scraper(header=headers)
    scrap.parse_shortage(drug_url)