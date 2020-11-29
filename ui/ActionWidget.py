from PySide2 import QtWidgets
from PySide2.QtCore import Slot, Signal, QSize
from PySide2.QtGui import QPixmap, QPalette, QColor, QFont
from PySide2.QtWidgets import QAction
from .ui_ActionWidget import Ui_ActionWidget
import platform


class ActionWidget(QtWidgets.QWidget, Ui_ActionWidget):

    def __init__(self, parent=None, action=None):
        super().__init__(parent)
        self.setupUi(self)
        self.action = action
        if not action:
            return
        print(action)
        self.label_name.setText(action.name)
        self.label_action_type.setText(action.action_type)
        self.label_text.setText(action.text)

        self.button_doit.clicked.connect(self.slot_on_do_it)

    @Slot()
    def slot_on_do_it(self):
        self.action.do_it()
