from PySide2 import QtWidgets
from PySide2.QtCore import Slot, Signal, QSize
from PySide2.QtGui import QPixmap, QPalette, QColor, QFont
from PySide2.QtWidgets import QAction
from .ui_CharacterWidget import Ui_CharacterWidget
import platform
from core.Character import *


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
        self.character.character_changed.connect(self.slot_on_character_changed)
        self.slot_on_character_changed()

    @Slot()
    def slot_on_character_changed(self, **kwargs):
        c = self.character
        s = f'{c.name} Efforts: {c.small_efforts} {c.medium_efforts} {c.large_efforts}\n'
        s += f'Cunning {c.cunning}'
        self.textEdit.setText(s)
        self.repaint()
