import sys
import os

from src.scraper.scrape import Scraper

def main():
    url = "https://www.imdb.com/list/ls053501318/"
    imdbScraper = Scraper()
    imdbScraper.getTopActors(url)

if __name__ == "__main__":
    main()