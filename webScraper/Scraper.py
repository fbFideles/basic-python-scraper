from urllib.request import urlopen
from bs4 import BeautifulSoup

class Scraper():
    def __init__(self, url):
        self.url = url

    def scrapPage(self):
        page = urlopen(self.url)
        soup = BeautifulSoup(page, 'html.parser')

        return soup