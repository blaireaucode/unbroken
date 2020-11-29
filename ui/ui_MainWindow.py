# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainWindow.ui',
# licensing of 'ui/MainWindow.ui' applies.
#
# Created: Sun Nov 29 10:59:12 2020
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
        self.widget_character = CharacterWidget(self.centralwidget)
        self.widget_character.setGeometry(QtCore.QRect(110, 80, 341, 201))
        self.widget_character.setObjectName("widget_character")
        self.widget_encounter = EncounterWidget(self.centralwidget)
        self.widget_encounter.setGeometry(QtCore.QRect(520, 320, 301, 201))
        self.widget_encounter.setObjectName("widget_encounter")
        self.widget_phase = PhaseWidget(self.centralwidget)
        self.widget_phase.setGeometry(QtCore.QRect(120, 310, 311, 211))
        self.widget_phase.setObjectName("widget_phase")
        self.button_new = QtWidgets.QPushButton(self.centralwidget)
        self.button_new.setGeometry(QtCore.QRect(10, 10, 61, 31))
        font = QtGui.QFont()
        self.button_new.setFont(font)
        self.button_new.setFlat(False)
        self.button_new.setObjectName("button_new")
        self.button_save = QtWidgets.QPushButton(self.centralwidget)
        self.button_save.setGeometry(QtCore.QRect(80, 10, 61, 31))
        font = QtGui.QFont()
        self.button_save.setFont(font)
        self.button_save.setFlat(False)
        self.button_save.setObjectName("button_save")
        self.widget_actions = ActionsWidget(self.centralwidget)
        self.widget_actions.setGeometry(QtCore.QRect(570, 90, 311, 191))
        self.widget_actions.setObjectName("widget_actions")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.button_new.setText(QtWidgets.QApplication.translate("MainWindow", "new", None, -1))
        self.button_save.setText(QtWidgets.QApplication.translate("MainWindow", "save", None, -1))

from .EncounterWidget import EncounterWidget
from .CharacterWidget import CharacterWidget
from .PhaseWidget import PhaseWidget
from .ActionsWidget import ActionsWidget
import unbroken_rc
