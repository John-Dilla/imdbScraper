from src.scraper.scrape import Scraper

import src.utility.tableHandler as d

class Controller:
    def __init__(self, url: str) -> None:
        self._topUrl = url
        self._scraper = Scraper()
    def structure(self):
        listTopFifty = self._scraper.getTopActors(self._topUrl)
        #for x in listTopFifty:
            #print(x["id"])
            #imdbScraper.getBio(x["ID"])
            #imdbScraper.getFilmography(x["ID"])
            #imdbScraper.getAwards(x["ID"])
        
        #Biography      imdbScraper.getBio("nm0000136")
        #Awards      imdbScraper.getAwards("nm0000136")
        #Filmography    imdbScraper.getFilmography("nm0000136")
        #Genres         imdbScraper.getGenres("nm0000136")

        #Overall Rating     d.ratingOverall("nm0000136")
        #Per Year Rating    d.ratingPerYear("nm0000136")
        
