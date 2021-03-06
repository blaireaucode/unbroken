from PySide2 import QtWidgets
from PySide2.QtCore import Slot
from .ui_TrickeryActionWidget import Ui_TrickeryActionWidget


class TrickeryActionWidget(QtWidgets.QWidget, Ui_TrickeryActionWidget):

    def __init__(self, game, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.game = game

        s = _('Trickery ? \n\n')
        s += _('You may now choose to trick the monster, avoiding '
               'combat entirely, if you can pay the Trickery Cost, '
               'which is listed on the monster sheet. Some monsters '
               'do not have a Trickery Cost and cannot be tricked.\n\n')
        s += _('If you trick the monster, you get no reward.')
        self.label_text.setText(s)

        self.button_trick.setText(_('Trick'))
        self.button_fight.setText(_('Fight !'))
        self.button_trick.clicked.connect(self.slot_on_trick)
        self.button_fight.clicked.connect(self.slot_on_fight)
        m = self.game.monster
        c = self.game.character
        if c.is_enough_resource(m.trickery):
            self.button_trick.setEnabled(True)
        else:
            self.button_trick.setEnabled(False)

    @Slot()
    def slot_on_trick(self):
        self.game.monster.trick()

    @Slot()
    def slot_on_fight(self):
        self.game.start_fight()
