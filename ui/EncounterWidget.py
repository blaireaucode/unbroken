from PySide2 import QtWidgets
from .ui_EncounterWidget import Ui_EncounterWidget


class EncounterWidget(QtWidgets.QWidget, Ui_EncounterWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.game = None

    def set_game(self, g):
        self.game = g
        if not g:
            self.textEdit.setText('No game')
            return
        self.game.phase_changed.connect(self.slot_on_phase_changed)
        self.slot_on_phase_changed()

    def slot_on_phase_changed(self, **kwargs):
        e = self.game.encounter
        if not e:
            self.textEdit.setText('No encounter')
        else:
            s = ''
            for ee in e:
                s += f'Encounter: {ee}\n'
            self.textEdit.setText(s)
        self.repaint()
