from bs4 import BeautifulSoup
import requests

class ScraperClient:
    def __init__(self):
        self.base_url = "https://books.toscrape.com/"
        self.headers = {
            "User-Agent" : "Mozilla/5.0"
        }

    def build_url(self, page_num):
        return f"{self.base_url}/catalogue/page-{page_num}.html"

    def fetch_html(self, url):
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()

        return response.text

    def make_soup(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    
