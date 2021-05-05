from src.scraper.scrape import Scraper

class Controller:
    def __init__(self, url: str) -> None:
        self.topUrl = url
    def structure(self):
        imdbScraper = Scraper()
        listTopFifty = imdbScraper.getTopActors(self.topUrl)
        """for x in listTopFifty:
            print(x["id"])
            imdbScraper.getBio(x["id"])
            imdbScraper.getFilmography(x["id"])"""
        
        imdbScraper.getBio("nm0001337")
        #imdbScraper.getBio("nm3910031")
        #imdbScraper.getBio("nm0842332")

        #imdbScraper.getFilmography("nm0001337")
        #imdbScraper.getFilmography("nm3910031")
        #imdbScraper.getFilmography("nm0842332")

        #imdbScraper.getAwards("nm0001337")