from PySide2 import QtWidgets
from PySide2.QtCore import Slot, Signal, QSize
from PySide2.QtGui import QPixmap, QPalette, QColor, QFont
from PySide2.QtWidgets import QAction
from .ui_ActionsWidget import Ui_ActionsWidget
import platform


class ActionsWidget(QtWidgets.QWidget, Ui_ActionsWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.game = None

    def set_game(self, g):
        self.game = g
        if not g:
            self.textEdit.setText('No game yet')
            return
        n = len(g.actions)
        self.textEdit.setText(f'Actions: {n}')