from .ui_ActionsWidget import Ui_ActionsWidget
from .GenericActionWidget import *
from .TravelDecisionActionWidget import *
from .ResolveOrRestActionWidget import *
from .ChooseEncounterActionWidget import *
from .CombatActionsWidget import *

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
        self.action_widgets = []
        # FIXME --> check phase and sub phase
        p = self.game.phase
        if p.is_travel:
            self.update_travel()
        if p.is_combat:
            self.update_combat()
        self.repaint()

    def update_combat(self):
        wa = CombatActionsWidget(self.game, self)
        self.action_layout.addWidget(wa)
        self.action_widgets.append(wa)

    def update_travel(self):
        sp = self.game.sub_phase
        if sp.is_preparation_step:
            self.update_travel_preparation()
        if sp.is_decision_step:
            self.update_travel_decision()
        if sp.is_exploration_step:
            self.update_travel_exploration()

    def update_travel_preparation(self):
        # all character abilities
        for a in self.game.character.abilities:
            wa = GenericActionWidget(self, a)
            self.action_layout.addWidget(wa)
            self.action_widgets.append(wa)
        # all possible actions in the current phase
        for a in self.game.all_actions:
            if not a.is_ability:
                wa = GenericActionWidget(self, a)
                self.action_layout.addWidget(wa)
                self.action_widgets.append(wa)

    def update_travel_decision(self):
        wa = TravelDecisionActionWidget(self.game, self)
        self.action_layout.addWidget(wa)
        self.action_widgets.append(wa)

    def update_travel_exploration(self):
        n = len(self.game.encounters)
        if n == 1:
            wa = ResolveOrRestActionWidget(self.game, self)
        else:
            wa = ChooseEncounterActionWidget(self.game, self)
        self.action_layout.addWidget(wa)
        self.action_widgets.append(wa)
