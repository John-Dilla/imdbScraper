import os
import sys
from PyQt5 import QtWidgets, uic

from src.scraper.scrapeController import Controller

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self._url = "https://www.imdb.com/list/ls053501318/"
        self._imdbScraper = Controller(self._url)

        # Call the inherited classes __init__ method
        super(MainWindow, self).__init__()         

        ui_path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(ui_path, "ui", "mainwindow.ui")
        # Load the .ui file
        uic.loadUi(path, self) 

        self.button_scrape.clicked.connect(self._scrape)

        self.show() # Show the GUI

    def _scrape(self) -> None:
        print("click worked")
        self._imdbScraper.structure()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()