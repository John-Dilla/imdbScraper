import time

from src.scraper.scrape import Scraper

import src.utility.tableHandler as d

class Controller:
    """This class is the controller of all scraping processes.
    It handles the calls and structurizes the processes.
    """

    def __init__(self, url: str) -> None:
        """Initialization of the Controller() class.

        Args:
            url (str): The URL to the top 50 list.
        """
        self._topUrl = url
        self._scraper = Scraper()

    def getTop(self) -> None:
        """ This function gets executed for the case when there is no database.
        Scrapes only the top 50 list, therefore no need for a return vale.
        """

        print("TOP 50 gets scraped")
        self._scraper.getTopActors(self._topUrl)

    def structure(self, progressCallback=None) -> None:
        """Structurizes the call of each scraping method.
        Retrieves every information on each entry in the top 50 list.
        """

        listTopFifty = self._scraper.getTopActors(self._topUrl)
        # Time stopped to track performance.
        start_time = time.time()

        totalCount = 1 + (len(listTopFifty) * 5)
        scrapeItems = 1

        if progressCallback:
            progressCallback(scrapeItems / totalCount * 100)

        # Scrape all information of each entry.
        for x in listTopFifty:
            print("ID:",x["ID"],"Name:",x["Name"])
            self._scraper.getBio(x["ID"])
            scrapeItems = scrapeItems + 1

            if progressCallback:
                progressCallback(scrapeItems / totalCount * 100)
                
            self._scraper.getFilmography(x["ID"])
            scrapeItems = scrapeItems + 1

            if progressCallback:
                progressCallback(scrapeItems / totalCount * 100)

            self._scraper.getAwards(x["ID"])
            scrapeItems = scrapeItems + 1

            if progressCallback:
                progressCallback(scrapeItems / totalCount * 100)

            self._scraper.getGenres(x["ID"])
            scrapeItems = scrapeItems + 1

            if progressCallback:
                progressCallback(scrapeItems / totalCount * 100)

            self._scraper.getPictures(x["ID"])
            scrapeItems = scrapeItems + 1

            if progressCallback:
                progressCallback(scrapeItems / totalCount * 100)

        # Duration of a all the scraping processes
        duration = time.time() - start_time
        print("Duration in seconds:", duration)

    def scrapeSingleActor(self, id: str) -> None:
        """Scrapes all information about a single actor or actress.
        This method is called when there's no information to be found
        in the database.

        Args:
            id (str): The IMDB-ID of an actor or actress.
        """

        self._scraper.getBio(id)
        self._scraper.getFilmography(id)
        self._scraper.getAwards(id)
        self._scraper.getGenres(id)
        self._scraper.getPictures(id)