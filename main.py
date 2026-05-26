import os

from scraper.fetch import fetch_html
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

    url = "https://books.toscrape.com/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

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
    html = fetch_html(url, headers)

    # =========================
    # Parse
    # =========================
    # main page title
    main_title = parse_title(html)
    print(f"Page title: {main_title}")

    # categories
    categories = parse_category(html)

    # products
    books = parse_product(html)

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
