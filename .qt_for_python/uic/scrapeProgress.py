# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\NonSystem\Dev\imdb\imdbScraper\src\controller\ui\scrapeProgress.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ScrapeDialog(object):
    def setupUi(self, ScrapeDialog):
        ScrapeDialog.setObjectName("ScrapeDialog")
        ScrapeDialog.setWindowModality(QtCore.Qt.WindowModal)
        ScrapeDialog.resize(566, 216)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ScrapeDialog.sizePolicy().hasHeightForWidth())
        ScrapeDialog.setSizePolicy(sizePolicy)
        ScrapeDialog.setModal(True)
        self.label = QtWidgets.QLabel(ScrapeDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(ScrapeDialog)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(10, 60, 541, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setFormat("%p%")
        self.progressBar.setObjectName("progressBar")
        self.buttonBeginScraping = QtWidgets.QPushButton(ScrapeDialog)
        self.buttonBeginScraping.setGeometry(QtCore.QRect(470, 170, 75, 23))
        self.buttonBeginScraping.setObjectName("buttonBeginScraping")
        self.label_2 = QtWidgets.QLabel(ScrapeDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 58, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(ScrapeDialog)
        QtCore.QMetaObject.connectSlotsByName(ScrapeDialog)

    def retranslateUi(self, ScrapeDialog):
        _translate = QtCore.QCoreApplication.translate
        ScrapeDialog.setWindowTitle(_translate("ScrapeDialog", "Dialog"))
        self.label.setText(_translate("ScrapeDialog", "IMDB Links"))
        self.buttonBeginScraping.setText(_translate("ScrapeDialog", "Start"))
        self.label_2.setText(_translate("ScrapeDialog", "currentURL"))
