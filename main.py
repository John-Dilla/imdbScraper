import sys
import os

from controller import Controller
import src.utility.file as f

def main():
    url = "https://www.imdb.com/list/ls053501318/"
    f.createDatabase()
    
    imdbScraper = Controller(url)
    imdbScraper.structure()

if __name__ == "__main__":
    main()