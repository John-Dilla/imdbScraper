import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

import src.utility.fileHandler as f

class Scraper:
    """This class provides the scraping methods."""
    def __init__(self) -> None:
        self._headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
                        'accept-language': 'en-US'}
                        #'accept-language': 'de-DE'}

    def getTopActors(self, url: str):
        r = requests.get(url, headers = self._headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        list = soup.find_all("h3",{"class": "lister-item-header"})

        listTop50 = []

        for item in list:
            tempDict = dict()
            tempDict['Ranking'] = item.span.getText().rstrip()
            tempDict['ID'] = item.a.get('href').split("?")[0].replace("/name/", "")
            tempDict['Name'] = item.a.getText().lstrip().rstrip("\n")
            listTop50.append(tempDict)


        dataFrame = pd.DataFrame(listTop50)
        f.writeToDirectory("", "top50", dataFrame)
        return listTop50

    def getBio(self, actorID: str):
        url = "https://www.imdb.com/name/" + actorID + "/bio?ref_=nm_ov_bio_sm"
        r = requests.get(url, headers = self._headers)
        soup = BeautifulSoup(r.text, 'html.parser')

        listBio = []

        birthPlace = None
        birthDate = None
        birthName = None
        nickName = None
        height = None
        bio = None
        spouse = None
        
        ### Info about birth gets scraped
        temp = soup.find_all('a', {'href': re.compile(r"search/name[/|]{,1}\?birth_place")})
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
            if x.td.text == "Nickname":
                nickName = x.td.next_sibling.text.strip('\n')
            if x.td.text == "Height":
                #print(x.td.next_sibling.next_sibling.text)
                height = x.td.next_sibling.next_sibling.text.strip('\n')

        ### Info about bio gets scraped
        temp = soup.find('div', {'class' : "soda odd"})
        bio = temp.p.text.lstrip().rstrip()
        

        ### Info about potential spouses gets scraped
        temp = soup.find(id='tableSpouses')
        ### check if actor has spouses
        if temp:
            tempListSpouse = []
            temp = temp.find_all('tr')
            for entry in temp:
                # Because of special a-tags some spouses have \xa0 characters
                entry = entry.text.strip().replace(u'\xa0', u' ').replace("\n", "")
                # The join operation removes multiple spaces
                entry = ' '.join(entry.split())
                entry = entry.replace("( ", "(")
                tempListSpouse.append(entry)
            spouse = "|".join(tempListSpouse)
        
        actorDict = {'Place of birth': birthPlace, 'Date of birth': birthDate,
        'Birthname': birthName, 'Nickname': nickName,
        'Height': height, 'Bio': bio, 'Spouse': spouse}
        
        listBio.append(actorDict)
        dataFrame = pd.DataFrame(listBio)
        f.writeToDirectory("biography", actorID, dataFrame)

    def getAwards(self, actorID: str):
        url = "https://www.imdb.com/name/" + actorID + "/awards?ref_=nm_ql_2"
        r = requests.get(url, headers = self._headers)
        soup = BeautifulSoup(r.text, 'html.parser')

        award = None
        awardYear = None
        awardOutcome = None
        awardDescription = None

        listAwards = []
        awardDict = dict()

        temp = soup.find_all('table', {"class": "awards"})
        
        for x in temp:
            #Award
            award = x.find_previous('h3').text.strip()

            years = x.find_all('tr')
            for y in years:
                awardExists = y.find('td', {"class": "award_year"})

                #Edge-Case for being nominated in multiple categories
                #would run into a None type if not checked
                if awardExists:
                    awardYear = awardExists.text.strip()
                    awardOutcome = y.find('td', {"class": "award_outcome"}).b.text.strip()
                
                #else:
                    #print("Year:", awardYear)
                    #print("Outcome:", awardOutcome)

                awardDescription_temp = y.find('td', {"class": "award_description"})
                if not awardDescription_temp.text == "\n":
                    #Description 
                    awardDescription = awardDescription_temp.next_element.strip()
                    #Movie + year 
                    if awardDescription_temp.find_next('a'):
                        mov = awardDescription_temp.find_next('a').text.strip()
                        year = awardDescription_temp.find_next('span').text.strip()
                        awardDescription = awardDescription + " - " + mov + " " + year
                        #print("###",awardDescription,"###")
                else:
                    awardDescription = None

                awardDict = {'Award': award, 'Year': awardYear,
                    'Outcome': awardOutcome, 'Description': awardDescription}

                #Generating the list
                listAwards.append(awardDict)

        dataFrame = pd.DataFrame(listAwards)
        f.writeToDirectory("awards", actorID, dataFrame)

    def getGenres(self, actorID: str):
        url = "https://www.imdb.com/filmosearch/?explore=title_type&role=" + actorID + "&ref_=nm_flmg_shw_3&sort=year,desc&mode=detail&page=1"
        r = requests.get(url, headers = self._headers)
        soup = BeautifulSoup(r.text, 'html.parser')

        listGenre = []
        
        genre = None
        dataCount = None

        temp = soup.find('div', {"class": "faceter-fieldset genres"}).find_all('input')
        for x in temp:
            genre = x['name']
            dataCount = x['data-count']
            awardDict = {'Genre': genre, 'Count': dataCount}
            listGenre.append(awardDict)

        dataFrame = pd.DataFrame(listGenre)
        f.writeToDirectory("filmography", "genre_"+actorID, dataFrame)    

    def getFilmography(self, actorID: str):
        #urlFilmographyAll is for scraping every imdb entry an actor/actress has
        #urlFilmographyAll = "&ref_=nm_flmg_shw_3&sort=user_rating,desc&mode=detail&page=1"
        urlFilmography = "&ref_=filmo_ref_typ&mode=detail&page=1&title_type=movie%2CtvMovie&sort=user_rating,desc"
        firstPage = "https://www.imdb.com/filmosearch/?explore=title_type&role=" + actorID + urlFilmography

        listFilmographyURL = []
        listFilmographyURL = self._getPages(firstPage, listFilmographyURL)

        listFilmography = []

        for url in listFilmographyURL:
            listFilmography = listFilmography + self._getFilmography(url)

        dataFrame = pd.DataFrame(listFilmography)
        f.writeToDirectory("filmography", actorID, dataFrame)

    def _getPages(self, url, listOfUrls):
        r = requests.get(url, headers = self._headers)
        soup = BeautifulSoup(r.text, 'html.parser')

        nextUrl = soup.find('a', class_ = "lister-page-next next-page")

        if nextUrl:
            listOfUrls.append(url)
            nextUrl = "https://www.imdb.com/filmosearch/" + nextUrl['href']
            return self._getPages(nextUrl, listOfUrls)
        else:
            listOfUrls.append(url)
            return listOfUrls


    def _getFilmography(self, url: str):
        r = requests.get(url, headers = self._headers)
        soup = BeautifulSoup(r.text, 'html.parser')

        ranking = None
        movieName = None
        movieYear = None
        # This is only needed for episodes, hence it's excluded from the dictionary
        movieNameSuffix = None

        certificate = None
        runtime = None
        genre = None
        rating = None
        plot = None

        listFilmography = []
        filmoDict = dict()

        temp = soup.find_all("div",{"class": "lister-item-content"})
        for x in temp:
            ranking = x.h3.span.text.strip("\n")
            #print(ranking)
            movieName = x.h3.a.text.strip()
            tempYear = x.a.find_next('span').text
            if re.findall(r"[\d]{4,}", tempYear):
                movieYear = re.findall(r"[\d]{4,}", tempYear)[0]
            else:
                movieYear = None
            if x.h3.small:                
                movieNameSuffix = x.h3.small.text.strip() + " " + x.h3.small.find_next('a').text.strip()
                #print("movieNameSuffix", movieNameSuffix)
            if x.p.find("span", {"class": "certificate"}):
                #This changes based on the 'accept-language' in the Request-Header
                certificate = x.find("span", {"class": "certificate"}).text.strip()
            else:
                certificate = None
            if x.find("span", {"class": "runtime"}):
                runtime = x.find("span", {"class": "runtime"}).text.strip()
            else:
                runtime = None
            if x.find("span", {"class": "genre"}):
                genre = x.find("span", {"class": "genre"}).text.strip()
            else:
                genre = None
            if x.find("div", {"class": "inline-block ratings-imdb-rating"}):
                rating = x.find("div", {"class": "inline-block ratings-imdb-rating"}).text.strip().replace(',', '.')
            else:
                rating = None
            if x.find("p", {"class": ""}):
                plot = x.find("p", {"class": ""}).text.strip()
                # Edge case where there is no existing plot
                if plot == "Add a Plot":
                    plot = None
                else:
                    # for cosmetic reasons - if existing - the extended summary is excluded from the plot
                    plot = plot.replace("See full summary\xa0»", "")
            else:
                plot = None

            filmoDict = {'Ranking': ranking, 'Name': movieName,
                'Year': movieYear, 'Certificate': certificate,
                'Runtime': runtime, 'Genre': genre, 'Rating': rating, 'Plot': plot}
            listFilmography.append(filmoDict)

        return listFilmography

    def getPictures(self, actorID: str):
        url = "https://www.imdb.com/name/" + actorID
        r = requests.get(url, headers = self._headers)
        soup = BeautifulSoup(r.text, 'html.parser')

        temp = soup.find_all("div", {"class": "image"})
        imageURL = temp[0].find_next("img")["src"]
        f.writeProfilepicture(actorID, imageURL)
