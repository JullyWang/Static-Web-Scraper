import requests

# define url + request's headers
url = "https://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print(f"Status code: {response.status_code}")
print(f"Headers: {response.headers}")
print(f"HTML Sample: {response.text[:300]}")