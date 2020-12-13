from PySide2 import QtWidgets
from PySide2.QtCore import Slot
from .ui_ResolveOrRestActionWidget import Ui_ResolveOrRestActionWidget
from core import *


class ResolveOrRestActionWidget(QtWidgets.QWidget, Ui_ResolveOrRestActionWidget):

    def __init__(self, game, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.game = game

        n = self.game.encounter[0].time
        s = _('Resolve or rest ?\n')
        s = s + ff(_('In all cases:, spend {n} Times.'))
        self.label_text.setText(s)

        self.button_resolve.setText(_('Resolve'))
        self.button_rest.setText(_('Rest'))
        self.button_resolve.clicked.connect(self.slot_on_resolve)
        self.button_rest.clicked.connect(self.slot_on_rest)
        e = self.game.encounter[0]
        c = self.game.character
        if c.is_enough_resource(e.spend):
            self.button_resolve.setEnabled(True)
        else:
            self.button_resolve.setEnabled(False)

    @Slot()
    def slot_on_resolve(self):
        self.game.encounter[0].resolve()
        self.game.after_encounter()

    @Slot()
    def slot_on_rest(self):
        self.game.encounter[0].rest()
        self.game.after_encounter()
