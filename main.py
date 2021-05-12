import sys
import os

from controller import Controller
from src.ui.mainWindow import MainWindow

import src.utility.fileHandler as f

def main():
    url = "https://www.imdb.com/list/ls053501318/"
    f.createDatabase()
    
    mainUI = MainWindow()

    #imdbScraper = Controller(url)
    #imdbScraper.structure()

if __name__ == "__main__":
    main()