from PySide2 import QtWidgets
from PySide2.QtCore import Slot, Signal, QSize
from PySide2.QtGui import QPixmap, QPalette, QColor, QFont
from PySide2.QtWidgets import QAction
from .ui_PhaseWidget import Ui_PhaseWidget
import platform


class PhaseWidget(QtWidgets.QWidget, Ui_PhaseWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.game = None

    def set_game(self, g):
        self.game = g
        if not g:
            self.textEdit.setText('no game')
            return
        self.game.phase_changed.connect(self.slot_on_phase_changed)
        self.slot_on_phase_changed()

    def slot_on_phase_changed(self, **kwargs):
        s = f'Phase: {self.game.phase.current_state}\n'
        s += f' step: {self.game.sub_phase.current_state}'
        self.textEdit.setText(s)
        self.repaint()