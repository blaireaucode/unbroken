from .ui_CombatActionsWidget import Ui_CombatActionsWidget
from .TrickeryActionWidget import *
from .BattleActionWidget import *


class CombatActionsWidget(QtWidgets.QWidget, Ui_CombatActionsWidget):

    def __init__(self, game, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.game = game
        self.action_widgets = []
        # remove debug widgets
        self.action_layout.removeWidget(self.debug1)
        self.action_layout.removeWidget(self.debug2)
        self.debug1.setVisible(False)
        self.debug2.setVisible(False)
        self.debug2.deleteLater()
        self.debug2.deleteLater()
        self.game.phase_changed.connect(self.update)
        self.update()

    def update(self, **kwargs):
        # remove previous
        for a in self.action_widgets:
            a.setVisible(False)
            self.action_layout.removeWidget(a)
        self.action_widgets = []
        if not self.game.phase.is_combat:
            return
        sp = self.game.sub_phase
        if sp.is_ambush_step:
            self.update_ambush()
        if sp.is_trickery_step:
            self.update_trickery()
        if sp.is_battle_step:
            self.update_battle()
        self.repaint()

    def update_ambush(self):
        pass

    def update_trickery(self):
        wa = TrickeryActionWidget(self.game, self)
        self.action_layout.addWidget(wa)
        self.action_widgets.append(wa)

    def update_battle(self):
        wa = BattleActionWidget(self.game, self)
        self.action_layout.addWidget(wa)
        self.action_widgets.append(wa)
