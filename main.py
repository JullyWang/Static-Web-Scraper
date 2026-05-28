import os

from scraper.client import ScraperClient
from scraper.fetch import fetch_html, make_soup
from scraper.parse import (
    parse_title,
    parse_category,
    parse_product
)
from scraper.export import export_csv

def main():
    # =========================
    # Config
    # =========================

    client = ScraperClient()

    base_dir = os.getcwd()

    category_file = os.path.join(
        base_dir,
        "data",
        "raw",
        "categories.csv"
    )

    product_file = os.path.join(
        base_dir,
        "data",
        "raw",
        "products.csv"
    )

    # =========================
    # Fetch
    # =========================

    html = fetch_html(client)
    soup = make_soup(client)

    # =========================
    # Parse
    # =========================
    # main page title
    main_title = parse_title(soup)
    print(f"Page title: {main_title}")

    # categories
    categories = parse_category(soup)

    # products
    books = parse_product(soup)

    # =========================
    # Export
    # =========================
    # categories
    export_csv(categories, category_file)

    # products
    export_csv(books, product_file)

    print("Export completed.")

if __name__ == "__main__":
    main()
