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
        
        # Retrieves the top 50 in case database does not exist (usually happens the very first time)
        self._imdbScraper.getTop()
        
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

        self.tableView.doubleClicked.connect(self._viewClicked)
        self.tableView.setSelectionBehavior(self.tableView.SelectRows)
                
        # Show the GUI
        self.show() 

    def _scrape(self) -> None:
        print("click worked")
        self._imdbScraper.structure()

    def _viewClicked(self, clickedIndex):
        print("worked")
        row=clickedIndex.row()
        model=clickedIndex.model()
        # Retrieve the id of the selected actress or actor
        model._df.iloc[[row]]["ID"]

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()