from PySide2 import QtWidgets
from PySide2.QtCore import Slot, Signal, QSize
from PySide2.QtGui import QPixmap, QPalette, QColor, QFont
from PySide2.QtWidgets import QAction
from .ui_CharacterWidget import Ui_CharacterWidget
import platform


class CharacterWidget(QtWidgets.QWidget, Ui_CharacterWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.game = None
        self.character = None

    def set_game(self, g):
        self.game = g
        if not g or not g.character:
            self.textEdit.setText('no character yet')
            return
        self.character = g.character
        self.textEdit.setText(self.character.name)
