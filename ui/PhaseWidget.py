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
