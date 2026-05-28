import argparse

def get_args():
    parser = argparse.ArgumentParser(
        prog="BookScraper",
        description="A simple scraper for static website."
    )

    # main title
    parser.add_argument('--title',
                         action='store_true',
                         help="Parse main site title")
    # categories
    parser.add_argument('--categories',
                         action='store_true',
                         help="Parse all categories and their link")
    # products
    parser.add_argument('--products',
                         action='store_true',
                         help="Parse all products on page")
    # pagination pages option
    parser.add_argument('--pages',
                        type=int,
                        help="Number of pages to scrape")
    # export option
    parser.add_argument('--export',
                        help="Export to file. Default csv")

    args = parser.parse_args()

    return args 