import sys
import os

from controller import Controller

def main():
    url = "https://www.imdb.com/list/ls053501318/"
    imdbScraper = Controller(url)
    imdbScraper.structure()

if __name__ == "__main__":
    main()