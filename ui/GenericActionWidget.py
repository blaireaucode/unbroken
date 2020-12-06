from PySide2 import QtWidgets
from PySide2.QtCore import Slot
from .ui_GenericActionWidget import Ui_GenericActionWidget


class GenericActionWidget(QtWidgets.QWidget, Ui_GenericActionWidget):

    def __init__(self, parent=None, action=None):
        super().__init__(parent)
        self.setupUi(self)
        self.action = action
        if not action:
            return
        self.label_name.setText(action.name)
        self.label_action_type.setText(action.action_type)
        self.label_text.setText(action.text)

        self.button_do_it.clicked.connect(self.slot_on_do_it)
        self.action.game.phase_changed.connect(self.slot_on_changed)
        self.action.game.character.character_changed.connect(self.slot_on_changed)
        self.slot_on_changed()

    def slot_on_changed(self, **kwargs):
        if self.action.is_applicable():
            self.button_do_it.setEnabled(True)
        else:
            self.button_do_it.setEnabled(False)
        self.repaint()

    @Slot()
    def slot_on_do_it(self):
        self.action.do_it()
