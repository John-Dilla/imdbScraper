import time

from src.scraper.scrape import Scraper

import src.utility.tableHandler as d

class Controller:
    def __init__(self, url: str) -> None:
        self._topUrl = url
        self._scraper = Scraper()
        self._scraper.getPictures("nm0000136")
    def structure(self):
        listTopFifty = self._scraper.getTopActors(self._topUrl)
        
        start_time = time.time()

        for x in listTopFifty:
            print(x["id"])
            self._scraper.getBio(x["ID"])
            self._scraper.getFilmography(x["ID"])
            self._scraper.getAwards(x["ID"])
            self._scraper.getGenres(x["ID"])

        # Duration of a all the scraping processes
        duration = time.time() - start_time
        print("Duration", duration)
        
        #Biography      
        self._scraper.getBio("nm0000136")
        #Awards      imdbScraper.getAwards("nm0000136")
        #Filmography    
        self._scraper.getFilmography("nm0000136")
        #Genres         imdbScraper.getGenres("nm0000136")

        #Overall Rating     d.ratingOverall("nm0000136")
        #Per Year Rating    d.ratingPerYear("nm0000136")
        
