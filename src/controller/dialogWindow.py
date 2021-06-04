from os.path import abspath

from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QDialog

from src.scraper.scrapeController import Controller

import src.utility.fileHandler as io


class ScrapeThread(QtCore.QThread):
    finished = QtCore.pyqtSignal()
    progress = QtCore.pyqtSignal(int)

    def __init__(self, scraper):
        super().__init__()
        self._imdbScraper = scraper


    def run(self):
        self._imdbScraper.structure(progressCallback=lambda current: self.progress.emit(int(current)))
        self.finished.emit()


class ScrapeDialog(QDialog):
    """Class for the dialog box about the scraping process.
    Shows the progress of the scraping process.

    Args:
        QDialog (QDialog): The Qt-Class from which this class inherites.
    """

    _backgroundTask: ScrapeThread = None

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

    def _scrapeFinished(self):
        self._backgroundTask = None
        self.buttonBeginScraping.setEnabled(True)


    def _startScraping(self) -> None:
        """Private method bound to the button which starts the whole 
        scraping process.
        """
        
        # Check if background task is running
        if self._backgroundTask is not None:
            # If still running, don't start a second scrape process
            return

        self._backgroundTask = ScrapeThread(self._imdbScraper)

        self._backgroundTask.finished.connect(self._scrapeFinished)

        self._backgroundTask.progress.connect(lambda current: [
            self.progressBar.setValue(current)
        ])

        self.buttonBeginScraping.setEnabled(False)
        self._backgroundTask.start()