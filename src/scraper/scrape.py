import requests
import re
from bs4 import BeautifulSoup

class Scraper:
    """This class provides the scraping methods."""
    def __init__(self) -> None:
        self._headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    def getTopActors(self, url: str):
        r = requests.get(url, headers = self._headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        list = soup.find_all("h3",{"class": "lister-item-header"})

        dictTop50 = []
        print(list)
        for item in list:
            #print("Top:{0} ID:{1} Name:{2}".format(item.span.getText(),
                #item.a.get('href'), item.a.getText().lstrip()))
            tempDict = dict()
            tempDict['top'] = item.span.getText().rstrip()
            tempDict['id'] = item.a.get('href').split("?")[0]
            tempDict['name'] = item.a.getText().lstrip().rstrip("\n")
            dictTop50.append(tempDict)

        print(dictTop50)

    def getBio(self, actorID: str):
        url = "https://www.imdb.com/" + actorID + "/bio?ref_=nm_ov_bio_sm"
        r = requests.get(url, headers = self._headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        list = soup.find_all(id='overviewTable')

        for item in list:
            #Born
            print(item.time.get('datetime'))
            print(item.time.next_sibling.next_sibling.getText())
            #Birth Name

            temp = item.find_all("td")
            for x in temp:
                print(str(x).strip("\n"))


