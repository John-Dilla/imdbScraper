from os.path import abspath

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

import src.utility.fileHandler as io


class About(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("About Me")
        self.setModal(True)

        # Load the .ui file
        pathUI = io.getUIPath(abspath(__file__), "aboutWindow.ui")
        uic.loadUi(pathUI, self) 

        self.show()