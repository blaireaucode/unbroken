from PySide2 import QtWidgets
from PySide2.QtCore import Slot
from .ui_ResolveOrRestActionWidget import Ui_ResolveOrRestActionWidget


class ResolveOrRestActionWidget(QtWidgets.QWidget, Ui_ResolveOrRestActionWidget):

    def __init__(self, game, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.game = game
        self.button_resolve.setText(_('Resolve'))
        self.button_rest.setText(_('Rest'))
        self.button_resolve.clicked.connect(self.slot_on_resolve)
        self.button_rest.clicked.connect(self.slot_on_rest)

    @Slot()
    def slot_on_resolve(self):
        pass
        # self.game.set_travel_phase_decision(True)

    @Slot()
    def slot_on_rest(self):
        pass
        # self.game.set_travel_phase_decision(False)
