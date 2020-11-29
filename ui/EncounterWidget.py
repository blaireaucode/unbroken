from PySide2 import QtWidgets
from PySide2.QtCore import Slot, Signal, QSize
from PySide2.QtGui import QPixmap, QPalette, QColor, QFont
from PySide2.QtWidgets import QAction
from .ui_EncounterWidget import Ui_EncounterWidget
import platform


class EncounterWidget(QtWidgets.QWidget, Ui_EncounterWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.game = None

    def set_game(self, g):
        self.game = g
        if not g:
            self.textEdit.setText('No encounter')
            return
        self.textEdit.setText(f'Encounter ...')
