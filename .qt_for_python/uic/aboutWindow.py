# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\NonSystem\Dev\imdb\imdbScraper\src\controller\ui\aboutWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.setWindowModality(QtCore.Qt.WindowModal)
        AboutDialog.resize(400, 300)
        AboutDialog.setMinimumSize(QtCore.QSize(400, 300))
        AboutDialog.setMaximumSize(QtCore.QSize(400, 300))
        self.label = QtWidgets.QLabel(AboutDialog)
        self.label.setGeometry(QtCore.QRect(60, 40, 281, 181))
        self.label.setObjectName("label")

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "About"))
        self.label.setText(_translate("AboutDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Bernhard Rippich, 3187269</span></p><p align=\"center\">IMDB-Scraper</p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">OTH-Regensburg</span></p></body></html>"))
