import requests

url = "https://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

res = requests.get(url, headers=headers)

print(f"Status code: {res.status_code}")
print(f"Headers: {res.headers}")
print(f"Sample HTML: {res.text[:500]}")