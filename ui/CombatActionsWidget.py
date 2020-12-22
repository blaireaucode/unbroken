from .ui_CombatActionsWidget import Ui_CombatActionsWidget
from .TrickeryActionWidget import *
from .BattleActionWidget import *


class CombatActionsWidget(QtWidgets.QWidget, Ui_CombatActionsWidget):

    def __init__(self, game, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.game = game
        self.action_widget = None
        self.game.phase_changed.connect(self.update)
        self.update()

    def update(self, **kwargs):
        # remove previous
        if self.action_widget:
            self.action_widget.setVisible(False)
            self.gridLayout.removeWidget(self.action_widget)
        self.action_widget = None
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
        self.action_widget = TrickeryActionWidget(self.game, self)

    def update_battle(self):
        self.action_widget = BattleActionWidget(self.game, self)
