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
        self.buttons = []
        for e in self.game.encounter:
            b = QtWidgets.QPushButton(self)
            self.verticalLayout.addWidget(b)
            b.setText(f(_('{e.name}')))
            b.clicked.connect(self.slot_pushed)
            self.buttons.append(b)

    @Slot()
    def slot_pushed(self):
        s = self.sender()
        idx = self.buttons.index(s)
        self.game.choose_encounter_card(idx)
