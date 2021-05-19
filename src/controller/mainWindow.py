import os
import sys
from PyQt5 import QtWidgets, uic

from src.scraper.scrapeController import Controller
from src.controller.model import PandasModel
import src.utility.fileHandler as io

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self._url = "https://www.imdb.com/list/ls053501318/"
        self._imdbScraper = Controller(self._url)
        
        # Call the inherited classes __init__ method
        super(MainWindow, self).__init__()         
        # Load the .ui file
        ui_path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(ui_path, "ui", "mainwindow.ui")
        uic.loadUi(path, self) 

        # Initialize button
        self.button_scrape.clicked.connect(self._scrape)

        # Initialize table
        df = io.getTable("", "top50")
        self._model = PandasModel(df)  
        self.tableView.setModel(self._model)
        self.tableView.setColumnHidden(0, True)
        
        # Show the GUI
        self.show() 

    def _scrape(self) -> None:
        print("click worked")
        self._imdbScraper.structure()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()