import os
from scraper.fetch import fetch_html
from scraper.parse import parse_title, parse_category
from scraper.export import export_csv

# define url + request's headers
url = "https://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# fetch html
html = fetch_html(url, headers)

# parse main title
main_title = parse_title(html)

# parse categories
categories = parse_category(html)

# export categories.csv
cwd = os.getcwd()
filename = cwd + '/data/raw/categories.csv'
export_csv(categories, filename)

