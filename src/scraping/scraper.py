# Main scraping script
import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, header):
        self.header = header

    def check_response(self, url):
        self.resp = requests.get(url=url, headers=self.header)
        return self.resp.status_code

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

        return file_url



# Check the swica drug directory for information on manufacturers and prices

# Check if there are any shortages known on drugshortage.ch
