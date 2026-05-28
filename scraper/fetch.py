from bs4 import BeautifulSoup
import requests

# fetch html and raise for error
def fetch_html(client):

    response = requests.get(
        client.base_url, 
        headers=client.headers, 
        timeout=10)
    try:
        response.raise_for_status()
        html = response.text
    except requests.exceptions.HTTPError as e:
        print("HTTP error occurred: ", e)
    except requests.exceptions.RequestException as e:
        print("A request error occurred: ", e)

    return html


def make_soup(client):
    html = fetch_html(client)
    soup = BeautifulSoup(html, 'html.parser')

    return soup


