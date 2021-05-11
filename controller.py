from src.scraper.scrape import Scraper

import src.utility.tableHandler as d

class Controller:
    def __init__(self, url: str) -> None:
        self.topUrl = url
    def structure(self):
        imdbScraper = Scraper()
        listTopFifty = imdbScraper.getTopActors(self.topUrl)
        #for x in listTopFifty:
            #print(x["id"])
            #imdbScraper.getBio(x["id"])
            #imdbScraper.getFilmography(x["id"])
            #imdbScraper.getAwards(x["id"])
        
        #imdbScraper.getFilmography("nm0000136")
        #imdbScraper.getGenres("nm0000136")

        print("Overall Rating", d.ratingOverall("nm0000136"))
        print(d.ratingPerYear("nm0000136"))
        
