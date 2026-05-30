from scraper.parse import parse_product

def pagination(client, args):

    max_pages = args.pages

    for page in range(1, max_pages + 1):

        url = client.build_url(page)
        html = client.fetch_html(url)
        soup = client.make_soup(html)
        books = parse_product(soup)


        print(f"Scraped page {page}")

        if not soup.find("li", class_="next"):
            break

    return books
