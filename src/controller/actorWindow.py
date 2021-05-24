import os

from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class Actor(QWidget):
    def __init__(self, actorID):
        super().__init__()

        # Call the inherited classes __init__ method
        super(Actor, self).__init__()         
        # Load the .ui file
        ui_path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(ui_path, "ui", "actorwindow.ui")
        uic.loadUi(path, self) 
