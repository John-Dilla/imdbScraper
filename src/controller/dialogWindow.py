from os.path import abspath

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

from src.scraper.scrapeController import Controller

import src.utility.fileHandler as io


class ScrapeDialog(QDialog):
    """Class for the dialog box about the scraping process.
    Shows the progress of the scraping process.

    Args:
        QDialog (QDialog): The Qt-Class from which this class inherites.
    """

    def __init__(self, imdbScraper: Controller):
        """Initializes the window and shows it to the user.

        Args:
            imdbScraper (Controller): Type of the scrape controller.
        """

        super().__init__()
        self._imdbScraper = imdbScraper

        # Load the .ui file
        pathUI = io.getUIPath(abspath(__file__), "scrapeProgress.ui")
        uic.loadUi(pathUI, self) 

        self.buttonBeginScraping.clicked.connect(self._startScraping)
        self.setWindowTitle("Scrape Progress")
        self.setModal(True)

        self.show()

    def _startScraping(self) -> None:
        """Private method bound to the button which starts the whole 
        scraping process.
        """

        self._imdbScraper.structure()