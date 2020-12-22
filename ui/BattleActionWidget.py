from .ui_BattleActionWidget import Ui_BattleActionWidget
from .GenericActionWidget import *


class BattleActionWidget(QtWidgets.QWidget, Ui_BattleActionWidget):

    def __init__(self, game, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.game = game
        self.game.phase_changed.connect(self.update)
        self.game.character.character_changed.connect(self.update)
        self.action_widgets = []
        # remove debug widgets
        self.action_layout.removeWidget(self.debug1)
        self.action_layout.removeWidget(self.debug2)
        self.debug1.setVisible(False)
        self.debug2.setVisible(False)
        self.debug2.deleteLater()
        self.debug2.deleteLater()
        # go
        self.update()

    def update(self, **kwargs):
        print(self.game.sub_phase)
        print(self.game.battle_phase)
        # remove previous
        for a in self.action_widgets:
            self.action_layout.removeWidget(a)
            a.setVisible(False)
        self.action_widgets = []
        # set current actions
        if self.game.battle_phase.is_character_step:
            self.update_character()
        if self.game.battle_phase.is_monster_step:
            self.update_monster()
        self.repaint()

    def update_monster(self):
        pass

    def update_character(self):
        actions = self.game.get_current_activities()
        for a in actions:
            wa = GenericActionWidget(self, a)
            self.action_layout.addWidget(wa)
            self.action_widgets.append(wa)
