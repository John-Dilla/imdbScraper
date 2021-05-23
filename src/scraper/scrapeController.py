import time

from src.scraper.scrape import Scraper

import src.utility.tableHandler as d

class Controller:
    def __init__(self, url: str) -> None:
        self._topUrl = url
        self._scraper = Scraper()

    def getTop(self):
        """ This function gets executed for the case when there is no database """
        self._scraper.getTopActors(self._topUrl)

    def structure(self):
        listTopFifty = self._scraper.getTopActors(self._topUrl)
        
        start_time = time.time()

        for x in listTopFifty:
            print("ID.",x["ID"],"Name",x["Name"])
            self._scraper.getBio(x["ID"])
            self._scraper.getFilmography(x["ID"])
            self._scraper.getAwards(x["ID"])
            self._scraper.getGenres(x["ID"])
            self._scraper.getPictures(x["ID"])

        # Duration of a all the scraping processes
        duration = time.time() - start_time
        print("Duration in seconds:", duration)
        
        #Overall Rating     d.ratingOverall("nm0000136")
        #Per Year Rating    d.ratingPerYear("nm0000136")    