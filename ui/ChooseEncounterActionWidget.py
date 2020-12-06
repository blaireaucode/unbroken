from PySide2 import QtWidgets
from PySide2.QtCore import Slot
from .ui_ChooseEncounterActionWidget import Ui_ChooseEncounterActionWidget
from inspect import currentframe


def f(s):
    frame = currentframe().f_back
    return eval(f"f'{s}'", frame.f_locals, frame.f_globals)


class ChooseEncounterActionWidget(QtWidgets.QWidget, Ui_ChooseEncounterActionWidget):

    def __init__(self, game, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.game = game
        e1 = self.game.encounter[0]
        e2 = self.game.encounter[1]
        self.button_first.setText(f(_('Choose {e1.name}')))
        self.button_second.setText(f(_('Choose {e2.name}')))
        self.button_first.clicked.connect(self.slot_on_first)
        self.button_second.clicked.connect(self.slot_on_second)

    @Slot()
    def slot_on_first(self):
        self.game.choose_encounter_card(0)

    @Slot()
    def slot_on_second(self):
        self.game.choose_encounter_card(1)
