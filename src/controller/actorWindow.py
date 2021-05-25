import os

from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class Actor(QWidget):
    def __init__(self, actorID):
        super().__init__()
        # Load the .ui file
        ui_path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(ui_path, "ui", "actor.ui")
        uic.loadUi(path, self) 
