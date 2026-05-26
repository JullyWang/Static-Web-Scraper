from bs4 import BeautifulSoup
import os
from scraper.parse import parse_title, parse_category, parse_product, parse_price
from scraper.fetch import fetch_html
from scraper.export import export_csv

# define url + request's headers
url = "https://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# fetch html
html = fetch_html(url, headers)

soup = BeautifulSoup(html, "html.parser")

# parse book price + available
products = parse_product(html, soup)
# export
cwd = os.getcwd()
product_file = cwd + '/data/raw/products.csv'
export_csv(products, product_file)