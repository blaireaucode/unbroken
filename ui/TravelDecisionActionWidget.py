from PySide2 import QtWidgets
from PySide2.QtCore import Slot
from .ui_TravelDecisionActionWidget import Ui_TravelDecisionActionWidget


class TravelDecisionActionWidget(QtWidgets.QWidget, Ui_TravelDecisionActionWidget):

    def __init__(self, game, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.game = game
        self.button_combat.setText(_('Yes! Start the combat ...'))
        self.button_exploration.setText(_('Not yet, explore!'))
        self.button_combat.clicked.connect(self.slot_on_combat)
        self.button_exploration.clicked.connect(self.slot_on_exploration)

    @Slot()
    def slot_on_combat(self):
        self.game.start_combat("trickery")

    @Slot()
    def slot_on_exploration(self):
        self.game.start_explore()
