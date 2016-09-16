import requests
from bs4 import BeautifulSoup

base_url = "https://en.wikipedia.org"
departure = "/wiki/J/22"
destination = "/wiki/Philosophy"
visited = [departure]
unwanted_elements = ["https", "http", "#", ".php",
                     ":", "(disambiguation)", "wikimedia"]


def getting_to_philosophy():
    """ Travel through wikipedia in search of Philosophy.

    Achieved by searching the current article for anchor tags and their
    respected href attributes. Then by process of elimination picking the next
    article to visit until destination (/wiki/Philosophy) has been reached.

    The first page is scraped outside of a while loop however once the
    departure page is finished with the page a while loop is used to keep
    checking if the destination has been visited.
    """

    # Fetch the desired page and its contents.
    response = requests.get(base_url + departure)
    # Turn the content into soup using the html parser.
    soup = BeautifulSoup(response.content, "html.parser")
    # Find the section of the page that is just the article.
    article = soup.find("div", id="bodyContent")
    # Find all of the paragraphs within the article as these contain the
    # anchors we are interested in.
    paragraphs = article.find_all("p")
    # Find all of the anchor tags within the paragraphs found above.
    anchors = [paragraph.find_all("a") for paragraph in paragraphs]
    # Get all of links excluding upper case links and coordinates.
    links = [link.get("href") for link in
             [anchor for sublist in anchors for anchor in sublist]
             if link.parent.get("id") != "coordinates" and link.text.islower()]
    # Further exclude links if the contain unwanted elements.
    for link in list(links):
        for element in unwanted_elements:
            if element in link:
                links.remove(link)
                break
    # Print the links contained within the page that and acceptable.
    print(links)

if __name__ == "__main__":
    getting_to_philosophy()
