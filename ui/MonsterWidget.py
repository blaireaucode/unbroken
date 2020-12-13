from PySide2 import QtWidgets
from .ui_MonsterWidget import Ui_MonsterWidget


class MonsterWidget(QtWidgets.QWidget, Ui_MonsterWidget):

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
        m = self.game.monster
        if not m:
            self.textEdit.setText('No Monster')
        else:
            self.textEdit.setText(f'Monster {m}')
        self.repaint()
