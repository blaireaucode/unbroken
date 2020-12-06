from PySide2 import QtWidgets
from PySide2.QtCore import Slot, Signal, QSize
from PySide2.QtGui import QPixmap, QPalette, QColor, QFont
from PySide2.QtWidgets import QAction
from .ui_NewGameWidget import Ui_NewGameWidget
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from .SlidingStackedWidget import *
from core import Game
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
        self.setModal(True)
        self.game = Game()
        self.current_character = None

        # build widget
        self.image_widgets = []
        self.characters = self.game.db.all_characters
        for c in self.characters:
            self.build_widget(c)

        # set widget to stacked
        self.slidingStacked = SlidingStackedWidget()
        self.slidingStacked.setWrap(True)
        for w in self.image_widgets:
            self.slidingStacked.addWidget(w)
        self.verticalLayout_2.replaceWidget(self.label, self.slidingStacked)
        # delete unused one, only useful to check in designer
        self.label.setVisible(False)
        self.label.deleteLater()
        self.previous.pressed.connect(self.slot_previous)
        self.next.pressed.connect(self.slot_next)
        self.change_current_character()

        # button text
        self.previous.setText(_('Previous'))
        self.next.setText(_('Next'))
        self.accepted.connect(self.slot_accepted)

    ## FIXME need exit -> build GAME

    @Slot()
    def slot_next(self):
        self.slidingStacked.slideInNext()
        self.change_current_character()

    @Slot()
    def slot_previous(self):
        self.slidingStacked.slideInPrev()
        self.change_current_character()

    def build_widget(self, character):
        l = QtWidgets.QLabel(self)
        l.setGeometry(QtCore.QRect(520, 50, 351, 461))
        l.setFrameShape(QtWidgets.QFrame.Box)
        l.setFrameShadow(QtWidgets.QFrame.Sunken)
        l.setText("")
        l.setFrameShape(QtWidgets.QFrame.NoFrame)
        l.setPixmap(QtGui.QPixmap(":/character/" + character.image))
        l.setAlignment(QtCore.Qt.AlignCenter)
        l.setObjectName(character.name)
        self.image_widgets.append(l)

    def change_current_character(self):
        i = self.slidingStacked.m_next  # not sure why 'next'
        c = self.characters[i]
        self.label_name.setText(c.name)
        self.label_class_type.setText(c.class_type.upper())
        self.label_index.setText(f'{i + 1}/{len(self.characters)}')
        self.change_current_abilities(c)
        self.current_character = c
        self.repaint()

    def change_current_abilities(self, character):
        # FIXME replace by a widget
        t = ''
        for a in character.abilities:
            t += f'{a.name} | {a.action_type}\n'
            t += f'{a.text}\n\n'
        self.label_ability.setText(t)

    def slot_accepted(self):
        print('accepted')
        self.game.set_character(self.current_character)
        #for a in Game.db.all_actions:
        #    a.set_game(self.game)
        self.game.phase.start()

