import requests

# fetch html and raise for error
def fetch_html(url, headers):
    response = requests.get(url, headers=headers, timeout=10)
    try:
        response.raise_for_status()
        html = response.text
    except requests.exceptions.HTTPError as e:
        print("HTTP error occurred: ", e)
    except requests.exceptions.RequestException as e:
        print("A request error occurred: ", e)

    return response.text
