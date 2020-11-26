from PySide2 import QtWidgets
from PySide2.QtCore import Slot, Signal, QSize
from PySide2.QtGui import QPixmap, QPalette, QColor, QFont
from PySide2.QtWidgets import QAction
from .ui_NewGameWidget import Ui_NewGameWidget
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from .SlidingStackedWidget import *
from core import *
import gettext

"""
Later: manage difficulty

Easy
This difficulty setting is for players who are finding NORMAL to be too challenging or who want to have an easier time while learning to play. On EASY, you roll the six-sided die once during setup to determine an extra
starting resource: metal (1), wood (2), food (3), cunning (4), medium effort (5), or treasure (6). You also begin the game with a skill card – draw two and select one, then put the other in the discard pile.

Normal
This is the standard difficulty setting.

Hard
This difficulty setting is for players who want a real challenge. On HARD, you begin the game with only 10 small effort, instead of 13. In addition, monsters attack first during combat.

"""


class NewGameWidget(QtWidgets.QDialog, Ui_NewGameWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # read database of character
        self.characters = read_character_database()
        # build widget

        # make ui (delete unused one)
        self.verticalLayout_2.removeWidget(self.label)
        self.label.deleteLater()

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(520, 50, 351, 461))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/character/sneak.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setGeometry(QtCore.QRect(520, 50, 251, 461))
        self.label2.setFrameShape(QtWidgets.QFrame.Box)
        self.label2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label2.setText("")
        self.label2.setPixmap(QtGui.QPixmap(":/character/sneak.png"))
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")

        # self.verticalLayout_2.addWidget(self.label)

        # set widget to stacked
        self.slidingStacked = SlidingStackedWidget()
        self.slidingStacked.addWidget(self.label)
        self.slidingStacked.addWidget(self.label2)

        self.verticalLayout_2.addWidget(self.slidingStacked)

        self.previous.pressed.connect(self.slot_previous)
        self.next.pressed.connect(self.slot_next)

        self.next.setText(_('Next'))

    @Slot()
    def slot_next(self):
        print('next')
        for c in self.characters:
            print(c)
        self.slidingStacked.slideInNext()

    @Slot()
    def slot_previous(self):
        print('previous')
        for c in self.characters:
            print(c)
        self.slidingStacked.slideInPrev()