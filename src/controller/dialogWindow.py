from os.path import abspath

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

import src.utility.fileHandler as io


class ScrapeDialog(QDialog):
    def __init__(self, imdbScraper):
        super().__init__()
        self._imdbScraper = imdbScraper

        # Load the .ui file
        pathUI = io.getUIPath(abspath(__file__), "scrapeProgress.ui")
        uic.loadUi(pathUI, self) 

        self.buttonBeginScraping.clicked.connect(self._startScraping)
        self.setWindowTitle("Scrape Progress")
        self.setModal(True)

        self.show()

    def _startScraping(self):
        self._imdbScraper.structure()
        #self._imdbScraper.test()