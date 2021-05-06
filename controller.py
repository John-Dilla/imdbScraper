from src.scraper.scrape import Scraper

class Controller:
    def __init__(self, url: str) -> None:
        self.topUrl = url
    def structure(self):
        imdbScraper = Scraper()
        listTopFifty = imdbScraper.getTopActors(self.topUrl)
        for x in listTopFifty:
            print(x["id"])
            #imdbScraper.getBio(x["id"])
            imdbScraper.getFilmography(x["id"])
            #imdbScraper.getAwards(x["id"])
        
        #imdbScraper.getFilmography("nm0001337")
        # imdbScraper.getBio("nm0001337")

        #imdbScraper.getAwards("nm0001337")