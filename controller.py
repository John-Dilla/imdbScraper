from src.scraper.scrape import Scraper

class Controller:
    def __init__(self, url: str) -> None:
        self.topUrl = url
    def structure(self):
        imdbScraper = Scraper()
        listTopFifty = imdbScraper.getTopActors(self.topUrl)
        for x in listTopFifty:
            print(x["id"])
            imdbScraper.getBio(x["id"])
        
        #imdbScraper.getBio("name/nm0001337")
        #imdbScraper.getBio("name/nm3910031")
        #imdbScraper.getBio("name/nm0842332")