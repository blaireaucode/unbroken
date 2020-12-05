from PySide2 import QtWidgets
from PySide2.QtCore import Slot
from .ui_TravelDecisionWidget import Ui_TravelDecisionWidget


class TravelDecisionWidget(QtWidgets.QWidget, Ui_TravelDecisionWidget):

    def __init__(self, game, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.game = game
        self.action = next(x for x in self.game.all_actions if x.id == 10)
        # self.label_name.setText(self.action.name)

        self.button_combat.clicked.connect(self.slot_on_combat)
        self.button_exploration.clicked.connect(self.slot_on_exploration)
        # self.action.game.character.character_changed.connect(self.slot_on_character_changed)
        # self.action.game.phase_changed.connect(self.slot_on_character_changed)
        # self.slot_on_character_changed()

    @Slot()
    def slot_on_combat(self):
        self.game.set_travel_phase_decision(True)

    @Slot()
    def slot_on_exploration(self):
        self.game.set_travel_phase_decision(False)
