from os.path import abspath

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

import src.utility.fileHandler as io


class About(QDialog):
    """Class for the dialog box about window.
    Shows basic information 

    Args:
        QDialog (QDialog): The Qt-Class from which this class inherites.
    """

    def __init__(self):
        """Initializes the window and shows it to the user.
        """

        super().__init__()
        
        self.setWindowTitle("About Me")
        self.setModal(True)

        # Load the .ui file
        pathUI = io.getUIPath(abspath(__file__), "aboutWindow.ui")
        uic.loadUi(pathUI, self) 

        self.show()