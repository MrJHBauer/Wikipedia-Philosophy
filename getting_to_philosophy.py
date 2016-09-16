import requests
from bs4 import BeautifulSoup

base_url = "https://en.wikipedia.org"
departure = "/wiki/J/22"
destination = "/wiki/Philosophy"
visited = [departure]
unwanted_elements = ["https", "http", "#", ".php", ":", "(disambiguation)", "wikimedia"]


def getting_to_philosophy():
    pass

if __name__ == "__main__":
    getting_to_philosophy()
