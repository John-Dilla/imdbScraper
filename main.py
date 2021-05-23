import sys
from PyQt5 import QtWidgets

from src.controller.mainWindow import MainWindow

import src.utility.fileHandler as io

def main():    
    #Create and structure database if it does not exist
    io.createDatabase()

    app = QtWidgets.QApplication(sys.argv)
    mainUI = MainWindow()
    app.exec_() 

if __name__ == "__main__":
    main()