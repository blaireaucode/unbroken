# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainWindow.ui',
# licensing of 'ui/MainWindow.ui' applies.
#
# Created: Sun Dec 13 14:56:16 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1455, 808)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_new = QtWidgets.QPushButton(self.centralwidget)
        self.button_new.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        self.button_new.setFont(font)
        self.button_new.setFlat(False)
        self.button_new.setObjectName("button_new")
        self.horizontalLayout.addWidget(self.button_new)
        self.button_save = QtWidgets.QPushButton(self.centralwidget)
        self.button_save.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        self.button_save.setFont(font)
        self.button_save.setFlat(False)
        self.button_save.setObjectName("button_save")
        self.horizontalLayout.addWidget(self.button_save)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.widget_character = CharacterWidget(self.centralwidget)
        self.widget_character.setMinimumSize(QtCore.QSize(300, 0))
        self.widget_character.setObjectName("widget_character")
        self.gridLayout.addWidget(self.widget_character, 0, 0, 1, 1)
        self.widget_actions = ActionsWidget(self.centralwidget)
        self.widget_actions.setMinimumSize(QtCore.QSize(300, 300))
        self.widget_actions.setObjectName("widget_actions")
        self.gridLayout.addWidget(self.widget_actions, 0, 1, 1, 1)
        self.widget_monster = MonsterWidget(self.centralwidget)
        self.widget_monster.setMinimumSize(QtCore.QSize(300, 300))
        self.widget_monster.setObjectName("widget_monster")
        self.gridLayout.addWidget(self.widget_monster, 0, 2, 2, 1)
        self.widget_phase = PhaseWidget(self.centralwidget)
        self.widget_phase.setMinimumSize(QtCore.QSize(300, 0))
        self.widget_phase.setObjectName("widget_phase")
        self.gridLayout.addWidget(self.widget_phase, 1, 0, 1, 1)
        self.widget_encounter = EncounterWidget(self.centralwidget)
        self.widget_encounter.setMinimumSize(QtCore.QSize(300, 300))
        self.widget_encounter.setObjectName("widget_encounter")
        self.gridLayout.addWidget(self.widget_encounter, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
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

from .MonsterWidget import MonsterWidget
from .EncounterWidget import EncounterWidget
from .ActionsWidget import ActionsWidget
from .CharacterWidget import CharacterWidget
from .PhaseWidget import PhaseWidget
import unbroken_rc
