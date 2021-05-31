from os.path import abspath

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtWidgets
from PyQt5 import uic
from PyQt5.QtGui import QPixmap

import pandas as pd

from src.controller.model import PandasModel
from src.scraper.scrapeController import Controller
import src.utility.fileHandler as io
import src.utility.tableHandler as th

class Actor(QWidget):
    """The class to show the window for an actor or actress.

    Args:
        QWidget (QWidget): The type of the window.
    """

    def __init__(self, actorID: str) -> None:
        """Initializes the UI window of an actor or actress.

        Args:
            actorID (str): The IMDB-ID of an actor or actress.
        """

        super().__init__()
        self._actorID = actorID
        self._modelRatings = None
        try:
            PandasModel(th.ratingPerYear(actorID))
        except OSError:
            # database for this actor is empty
            print("Actor or Actress has not been scraped before.")
            _scraper = Controller("")
            _scraper.scrapeSingleActor(actorID)

        self._modelRatings = PandasModel(th.ratingPerYear(actorID))

        self._dfGenres = io.getTable("filmography", "genre_"+actorID)
        self._modelGenres = PandasModel(self._dfGenres)

        self._dfAwards = io.getTable("awards", actorID)
        self._modelAwards = PandasModel(self._dfAwards)
        
        self._dfMovies = io.getTable("filmography", actorID)
        self._modelMovies = PandasModel(self._dfMovies)
        self._modelTop5 = PandasModel(th.top5Movie(actorID))

        # Load the .ui file
        pathUI = io.getUIPath(abspath(__file__), "actorWindow.ui")
        uic.loadUi(pathUI, self) 

        # Set the text for all the bio information labels 
        dfBio = io.getTable("biography", actorID)
        name = "Name: \n" + str(dfBio.iloc[0]["Birthname"])
        self.uiName.setText(name)

        icon = io.getUIPath(abspath(__file__), "rating.ico")
        rating = "Overall rating: <br>" + str(th.ratingOverall(actorID))
        self.uiRating.setText("<html>"+rating+" <img src='"+icon+"'></html>")

        # Place of birth
        place = "Place of Birth: \n" + str(dfBio.iloc[0]["Place of birth"])
        self.uiPlace.setText(place)
        # Date of birth
        birth = "Date of Birth: \n" + str(dfBio.iloc[0]["Date of birth"])
        self.uiDate.setText(birth)
        
        if not pd.isnull(dfBio.iloc[0]["Spouse"]):
            # Spouse. Also there must be a new line for each spouse
            tempListSpouse = str(dfBio.iloc[0]["Spouse"]).split('|')
            spouse = "Spouse: \n" + '\n'.join(tempListSpouse)
            self.uiSpouse.setText(spouse)
        else:
            # Hide spouse label if NaN
            self.uiSpouse.setVisible(False)
        # Height
        height = "Height: \n" + str(dfBio.iloc[0]["Height"])
        self.uiHeight.setText(height)

        # Set biography
        self.textBiography.setText(dfBio.iloc[0]["Bio"])
        self.textBiography.setReadOnly(True)
        # Set profile picture
        pixmap = QPixmap(io.getPicture(actorID))
        pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.picture.setPixmap(pixmap)        

        # Initialize movie table
        self._setupTableMovies()
        self.checkTop5.stateChanged.connect(self._clickBox)
        # Initialize award table
        self._setupTableAwards()       
        # Initialize genre table
        self._setupTableGenres()
        # Initialize overall rating table
        self._setupTableRating()
        
        self.show()

    def _setupTableAwards(self) -> None:
        """Private function to set up the award table.
        """

        self.tableAwards.setModel(self._modelAwards)
        self._generalTableSetup(self.tableAwards)
        self.tableAwards.setColumnHidden(0, True)

    def _setupTableMovies(self) -> None:
        """Private function to set up the movie table.
        """

        self.tableMovies.setModel(self._modelMovies)
        self._generalTableSetup(self.tableMovies)
        self.tableMovies.setColumnHidden(0, True)

        # hide the movie plot
        self.tableMovies.setColumnHidden(8, True)
        #plot = table column 8
        self.moviePlot.setVisible(False)
        self.moviePlot.setReadOnly(True)

        # Reacts on all table selection changes
        self.tableMovies.selectionModel().selectionChanged.connect(self._showPlot)

    def _showPlot(self):
        """Private function to outsource the plot of a movie in a seperate widget.
        Also, this function tracks the selected row and changes the plot accordingly.
        If the plot is not available, the box is set to setVisible(False).
        """

        # Use model
        model = self.tableMovies.model()
        # Get first selected row
        row = self.tableMovies.selectedIndexes()[0].row()

        if not pd.isnull(model._df.iloc[row]["Plot"]):
            plot = model._df.iloc[row]["Plot"]
            self.moviePlot.setText(plot)
            self.moviePlot.setVisible(True)
        else:
            self.moviePlot.setVisible(False)
    
    def _setupTableTop5(self):
        """Private function to set up the top 5 movie table.
        """

        self.tableMovies.setModel(self._modelTop5)
        self._generalTableSetup(self.tableMovies)

    def _setupTableGenres(self):
        """Private function to set up the genre table.
        """

        self.tableGenres.setModel(self._modelGenres)
        self._generalTableSetup(self.tableGenres)
        self.tableGenres.setColumnHidden(0, True)

    def _setupTableRating(self):
        """Private function to set up the rating per year table.
        """

        self.tableRating.setModel(self._modelRatings)
        self._generalTableSetup(self.tableRating)

    def _generalTableSetup(self, table):
        """Private function to set up the general properties of any table.
        """

        table.setSelectionBehavior(table.SelectRows)
        header = table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

    def _clickBox(self, state):
        """Private function to set up a checkbox.
        Implemented to toggle between the movie table and the top 5 movie table.
        """

        self.moviePlot.setVisible(False)
        if state == QtCore.Qt.Checked:
            print('Checked')
            self._setupTableTop5()
        else:
            print('Unchecked')
            self._setupTableMovies()