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
        for item in list:
            #print("Top:{0} ID:{1} Name:{2}".format(item.span.getText(),
                #item.a.get('href'), item.a.getText().lstrip()))
            tempDict = dict()
            tempDict['top'] = item.span.getText().rstrip()
            tempDict['id'] = item.a.get('href').split("?")[0]
            tempDict['name'] = item.a.getText().lstrip().rstrip("\n")
            print(tempDict)
            dictTop50.append(tempDict)

        return dictTop50

    def getBio(self, actorID: str):
        url = "https://www.imdb.com/" + actorID + "/bio?ref_=nm_ov_bio_sm"
        r = requests.get(url, headers = self._headers)
        soup = BeautifulSoup(r.text, 'html.parser')

        birthPlace = ""
        birthDate = ""
        birthName = ""
        nickName = ""
        height = ""
        bio = ""
        spouse = ""
        
        ### Info about birth gets scraped
        temp = soup.find_all('a', {'href':re.compile(r"search/name[/|]{,1}\?birth_place")})
        if temp:
            birthPlace = temp[0].text
            temp = soup.find(id='overviewTable')
            birthDate = temp.time.get('datetime')
        else:
            print("array empty")
        

        ### Info about name, nickname and height gets scraped
        table = soup.find(id='overviewTable').find_all('tr')
        for x in table:
            if x.td.text == "Birth Name":
                birthName = x.td.next_sibling.text.strip('\n')
                #print(birthName)
            if x.td.text == "Nickname":
                nickName = x.td.next_sibling.text.strip('\n')
                #print(nickName)
            if x.td.text == "Height":
                #print(x.td.next_sibling.next_sibling.text)
                height = x.td.next_sibling.next_sibling.text.strip('\n')
                #print(height)

        ### Info about bio gets scraped
        temp = soup.find('div', {'class' : "soda odd"})
        bio = temp.p.text.lstrip().rstrip()
        

        ### Info about potential spouses gets scraped
        temp = soup.find(id='tableSpouses')
        ### check if actor has spouses
        if temp:
            temp = temp.find_all('tr')
            for x in temp:
                #print(x.td.a.text, "--------------> Spouse")
                entries = x.find_all('td')
                for y in entries:
                    spouse = spouse + " ".join(y.text.split()) + " "
                #print(spouse)
        
        
        
        actorDict = {'Place of birth': birthPlace, 'Date of birth': birthDate,
        'Birthname': birthName, 'Nickname': nickName,
        'Height': height, 'Bio': bio, 'Spouse': spouse}
        
        
        #for key, value in actorDict.items():
        #    print(key, ' : ', value)


        return actorDict