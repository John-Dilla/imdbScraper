import time

from src.scraper.scrape import Scraper

import src.utility.tableHandler as d

class Controller:
    def __init__(self, url: str) -> None:
        self._topUrl = url
        self._scraper = Scraper()

    def getTop(self):
        """ This function gets executed for the case when there is no database """
        print("TOP 50 gets scraped")
        self._scraper.getTopActors(self._topUrl)

    def structure(self):
        listTopFifty = self._scraper.getTopActors(self._topUrl)
        
        start_time = time.time()

        for x in listTopFifty:
            print("ID:",x["ID"],"Name:",x["Name"])
            self._scraper.getBio(x["ID"])
            self._scraper.getFilmography(x["ID"])
            self._scraper.getAwards(x["ID"])
            self._scraper.getGenres(x["ID"])
            self._scraper.getPictures(x["ID"])

        # Duration of a all the scraping processes
        duration = time.time() - start_time
        print("Duration in seconds:", duration)

    def scrapeSingleActor(self, id):
        self._scraper.getBio(id)
        self._scraper.getFilmography(id)
        self._scraper.getAwards(id)
        self._scraper.getGenres(id)
        self._scraper.getPictures(id)
        
    def test(self):
        self._scraper.getAwards("nm0001401")