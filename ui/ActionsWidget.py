from PySide2 import QtWidgets
from PySide2.QtCore import Slot, Signal, QSize
from PySide2.QtGui import QPixmap, QPalette, QColor, QFont
from PySide2.QtWidgets import QAction
from .ui_ActionsWidget import Ui_ActionsWidget
import platform
from .ActionWidget import *


class ActionsWidget(QtWidgets.QWidget, Ui_ActionsWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.game = None
        self.action_widgets = []
        # remove debug widgets
        self.action_layout.removeWidget(self.debug1)
        self.action_layout.removeWidget(self.debug2)
        self.debug1.setVisible(False)
        self.debug2.setVisible(False)
        self.debug2.deleteLater()
        self.debug2.deleteLater()

    def set_game(self, g):
        self.game = g
        if not g:
            #self.textEdit.setText('No game yet')
            return
        n = len(g.actions)
        m = len(g.db.all_abilities)
        # self.textEdit.setText(f'Actions: {n} (among {m})')
        self.update()

    def update(self):
        # update list of available actions according to phase
        p = self.game.phase
        if not p.is_travel:
            self.textEdit.setText(f'Actions todo {p.current_state}')
            return
        # list of available actions (txt for debug)
        s = f'Available actions:\n'
        for a in self.game.character.abilities:
            s += f'Abilities: {a.name}\n'
        for a in self.game.db.all_abilities:
            if a.action_type == 'General' or a.action_type == 'Travel':
                s += f'General action: {a.name}\n'
        print(s)
        # self.textEdit.setText(s)
        # action widgets
        for a in self.game.character.abilities:
            # FIXME 'ask' action if available now
            wa = ActionWidget(self, a)
            self.action_layout.addWidget(wa)
            self.action_widgets.append(wa)
        self.repaint()
