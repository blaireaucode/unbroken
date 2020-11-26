# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainWindow.ui',
# licensing of 'ui/MainWindow.ui' applies.
#
# Created: Thu Nov 26 21:27:08 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1008, 628)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.character = CharacterWidget(self.centralwidget)
        self.character.setGeometry(QtCore.QRect(100, 130, 341, 201))
        self.character.setObjectName("character")
        self.encouter = EncounterWidget(self.centralwidget)
        self.encouter.setGeometry(QtCore.QRect(560, 80, 301, 171))
        self.encouter.setObjectName("encouter")
        self.phase = PhaseWidget(self.centralwidget)
        self.phase.setGeometry(QtCore.QRect(540, 300, 371, 241))
        self.phase.setObjectName("phase")
        self.button_new = QtWidgets.QPushButton(self.centralwidget)
        self.button_new.setGeometry(QtCore.QRect(10, 10, 61, 31))
        font = QtGui.QFont()
        self.button_new.setFont(font)
        self.button_new.setFlat(False)
        self.button_new.setObjectName("button_new")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.button_new.setText(QtWidgets.QApplication.translate("MainWindow", "new", None, -1))

from .EncounterWidget import EncounterWidget
from .CharacterWidget import CharacterWidget
from .PhaseWidget import PhaseWidget
