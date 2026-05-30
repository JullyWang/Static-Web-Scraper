import os

from cli import get_args
from scraper.client import ScraperClient
from scraper.fetch import fetch_html, make_soup
from scraper.parse import parse_title, parse_category, parse_product
from scraper.pagination import pagination
from scraper.export import export_csv


def main():
    # =========================
    # Config
    # =========================

    base_dir = os.getcwd()

    category_file = os.path.join(base_dir, "data", "raw", "categories.csv")

    product_file = os.path.join(base_dir, "data", "raw", "products.csv")

    # =========================
    # Fetch + Make Soup
    # =========================

    # Client instance
    client = ScraperClient()

    html = fetch_html(client)
    soup = make_soup(client)

    # =========================
    # Parse + Export
    # =========================

    # get arguments from argparse
    args = get_args()

    # main page title
    if args.title:
        main_title = parse_title(soup)
        print(f"Page title: {main_title}")

    if args.categories:
        # categories
        categories = parse_category(soup)
        print(f"[INFO] Successfully parsed {len(categories)} categories")

        if args.export == "csv":
            export_csv(categories, category_file)
            print("[INFO] Export completed!")

    if args.products:
        # products
        products = parse_product(soup)
        print(f"[INFO] Successfully parsed {len(products)} categories")

        if args.export == "csv":
            export_csv(products, product_file)
            print("[INFO] Export completed!")

    # =========================
    # Pagination
    # =========================

    if args.pages:
        pag_books = pagination(client, args)
        print(f"[INFO] Successfully parsed {len(pag_books)} categories")
        if args.export == "csv":
            export_csv(pag_books, product_file)
            print("[INFO] Export completed!")
        else:
            print("Successfully parse, add '--export' option to save file")


if __name__ == "__main__":
    main()
