from bs4 import BeautifulSoup

def parse_title(html):
    soup = BeautifulSoup(html, "html.parser")

    return soup.title.text.strip()

def parse_category(html):
    data = []

    soup = BeautifulSoup(html, "html.parser")

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