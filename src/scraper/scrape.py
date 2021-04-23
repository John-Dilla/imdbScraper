import requests
import re
from bs4 import BeautifulSoup

class Scraper:
    """This private class is the Logger instance SingletonObject holds."""
    def __init__(self) -> None:
        self.headers = headers = {'user-agent': 'my-app/0.0.1'}

    def getTopActors(self, url: str):
        r = requests.get(url, headers = self.headers)
        print(r.text)