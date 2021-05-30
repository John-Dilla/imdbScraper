import sys
from PyQt5 import QtWidgets

from src.controller.mainWindow import MainWindow

import src.utility.fileHandler as io

from src.scraper.scrapeController import Controller

def main() -> None:
    """The main function. Starts up the application and creates the database.
    """
    io.createDatabase()

    app = QtWidgets.QApplication(sys.argv)
    mainUI = MainWindow()
    mainUI.show()
    app.exec_() 
    #test = Controller("https://www.imdb.com/list/ls053501318/")
    #test.test()


if __name__ == "__main__":
    main()