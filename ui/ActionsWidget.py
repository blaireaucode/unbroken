from PySide2 import QtWidgets
from PySide2.QtCore import Slot, Signal, QSize
from PySide2.QtGui import QPixmap, QPalette, QColor, QFont
from PySide2.QtWidgets import QAction
from .ui_ActionsWidget import Ui_ActionsWidget
import platform
from .ActionWidget import *
from .TravelDecisionWidget import *

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
        self.game.character.character_changed.connect(self.update)
        self.game.phase_changed.connect(self.update)
        self.update()

    def update(self, **kwargs):
        # remove previous
        for a in self.action_widgets:
            a.setVisible(False)
            self.action_layout.removeWidget(a)
            #a.deleteLater()
        self.action_widgets = []
        # FIXME --> check phase and sub phase
        p = self.game.phase
        sp = self.game.sub_phase
        print(p, sp)
        if not p.is_travel:
            self.repaint()
            return
        if p.is_travel and sp.is_preparation_step:
            self.update_travel()
        if p.is_travel and sp.is_decision_step:
            self.update_decision()
        self.repaint()

    def update_travel(self):
        for a in self.game.character.abilities:
            wa = ActionWidget(self, a)
            self.action_layout.addWidget(wa)
            self.action_widgets.append(wa)
        for a in self.game.all_actions:
            if not a.is_ability:
                wa = ActionWidget(self, a)
                self.action_layout.addWidget(wa)
                self.action_widgets.append(wa)

    def update_decision(self):
        a = next(x for x in self.game.all_actions if x.id == 10)
        wa = TravelDecisionWidget(self.game, self)
        self.action_layout.addWidget(wa)
        self.action_widgets.append(wa)
