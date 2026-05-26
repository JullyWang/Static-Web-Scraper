from bs4 import BeautifulSoup
from scraper.fetch import fetch_html
from scraper.utils.cleaner import clean_price

# define url + request's headers
url = "https://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# make soup
html = fetch_html(url, headers)
soup = BeautifulSoup(html, "html.parser")

def parse_title(html, soup):

    return soup.title.text.strip()

def parse_category(html, soup):
    data = []

    categories = soup.find("div", class_="side_categories")
    links = categories.find_all("a")

    for cat in links[1:]:
        title = cat.get_text(strip=True)
        href = cat.get("href")

        data.append({
    "category": title,
    "link": href
})

    return data

def parse_product(html, soup):
    data = []

    blocks = soup.find_all("article", class_="product_pod")
    for block in blocks:
        book_tag = block.find("h3")
        title = (book_tag.find("a")).get("title")
        link = (book_tag.find("a")).get("href")

        price_tag = block.find("p", class_="price_color")
        price = clean_price(price_tag.get_text())

        avail_tag = block.find("i", class_="icon-ok")
        status = avail_tag.get_text(strip=True)

        data.append({
            "book_title": title,
            "book_link": link,
            "price": price,
            "status": status
        })

        print(f"Successfully parsed {len(data)} products")
    
    return data


