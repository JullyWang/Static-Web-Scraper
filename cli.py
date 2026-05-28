import argparse

def get_args():
    parser = argparse.ArgumentParser(
        prog="BookScraper",
        description="A simple scraper for static website."
    )

    parser.add_argument('--title', action='store_true')
    parser.add_argument('--categories', action='store_true')
    parser.add_argument('--products', action='store_true')
    parser.add_argument('--export')

    args = parser.parse_args()

    return args 