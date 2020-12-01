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
            return
        self.update()

    def update(self):
        # update list of available actions according to phase
        p = self.game.phase
        if not p.is_travel:
            self.textEdit.setText(f'Actions todo {p.current_state}')
            return
        # action widgets
        for a in self.game.character.abilities:
            wa = ActionWidget(self, a)
            self.action_layout.addWidget(wa)
            self.action_widgets.append(wa)
        for a in self.game.all_actions:
            if not a.is_ability:
                wa = ActionWidget(self, a)
                self.action_layout.addWidget(wa)
                self.action_widgets.append(wa)
        self.repaint()
