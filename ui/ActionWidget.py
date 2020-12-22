from .ui_ActionWidget import Ui_ActionWidget
from .MultipleActionsWidget import *
from .TravelDecisionActionWidget import *
from .ResolveOrRestActionWidget import *
from .ChooseEncounterActionWidget import *
from .CombatActionsWidget import *


class ActionWidget(QtWidgets.QWidget, Ui_ActionWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.game = None
        self.action_widget = None

    def set_game(self, g):
        self.game = g
        if not g:
            return
        self.game.phase_changed.connect(self.update)
        self.update()

    def update(self, **kwargs):
        # remove previous
        if self.action_widget:
            self.action_widget.setVisible(False)
            self.gridLayout.removeWidget(self.action_widget)
        self.action_widget = None
        # split according to phase
        p = self.game.phase
        if p.is_travel:
            self.update_travel()
        if p.is_combat:
            self.update_combat()
        self.gridLayout.addWidget(self.action_widget)
        self.repaint()

    def update_combat(self):
        print('here)')
        self.action_widget = CombatActionsWidget(self.game, self)
        # FIXME -> singe TravelActionsWidget ?

    def update_travel(self):
        sp = self.game.sub_phase
        if sp.is_preparation_step:
            self.update_travel_preparation()
        if sp.is_decision_step:
            self.update_travel_decision()
        if sp.is_exploration_step:
            self.update_travel_exploration()

    def update_travel_preparation(self):
        self.action_widget = MultipleActionsWidget(self.game, self)

    def update_travel_decision(self):
        self.action_widget = TravelDecisionActionWidget(self.game, self)

    def update_travel_exploration(self):
        n = len(self.game.encounters)
        if n == 1:
            self.action_widget = ResolveOrRestActionWidget(self.game, self)
        else:
            self.action_widget = ChooseEncounterActionWidget(self.game, self)
