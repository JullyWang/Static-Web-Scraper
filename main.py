import os

from cli import get_args
from scraper.client import ScraperClient
from scraper.fetch import fetch_html, make_soup
from scraper.parse import parse_title, parse_category, parse_product
from scraper.pagination import pagination
from scraper.export import export_csv, export_excel


def main():
    # =========================
    # Config
    # =========================

    # base directory
    base_dir = os.getcwd()

    # csv file
    category_file = os.path.join(base_dir, "data", "raw", "categories.csv")
    product_file = os.path.join(base_dir, "data", "raw", "products.csv")

    # excel file
    category_excel = os.path.join(base_dir, "data", "raw", "categories.xlsx")
    product_excel = os.path.join(base_dir, "data", "raw", "products.xlsx")

    # =========================
    # Fetch + Make Soup
    # =========================

    # Client instance
    client = ScraperClient()

    # fetch and make soup
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

    # categories parse
    if args.categories:
        categories = parse_category(soup)
        print(f"[INFO] Successfully parsed {len(categories)} categories")

        # categories export
        if args.export == "csv":
            export_csv(categories, category_file)
            print("[INFO] Export to csv completed!")
        elif args.export == "excel":
            export_excel(categories, category_excel)
            print("[INFO] Export to excel completed!")
        else:
            print("Successfully parse, add '--export' option to save file")


    # products parse
    if args.products:
        products = parse_product(soup)
        print(f"[INFO] Successfully parsed {len(products)} categories")

        # product export
        if args.export == "csv":
            export_csv(products, product_file)
            print("[INFO] Export to csv completed!")
        elif args.export == "excel":
            export_excel(products, product_excel)
            print("[INFO] Export to excel completed!")
        else:
            print("Successfully parse, add '--export' option to save file")


    # =========================
    # Pagination
    # =========================

    if args.pages:
        pag_books = pagination(client, args)
        print(f"[INFO] Successfully parsed {len(pag_books)} categories")
        if args.export == "csv":
            export_csv(pag_books, product_file)
            print("[INFO] Export completed!")
        elif args.export == "excel":
            export_excel(pag_books, product_excel)
        else:
            print("Successfully parse, add '--export' option to save file")


if __name__ == "__main__":
    main()
