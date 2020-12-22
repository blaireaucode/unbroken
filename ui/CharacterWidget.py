from PySide2 import QtWidgets
from PySide2.QtCore import Slot
from .ui_CharacterWidget import Ui_CharacterWidget


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
        r = c.resources
        s = f'{c.name} Efforts: {r.small_efforts} {r.medium_efforts} {r.large_efforts}\n'
        s += f'Cunning {r.cunning}\n'
        s += f'Food {r.food}\n'
        s += f'Wood {r.wood}\n'
        s += f'Metal {r.metal}\n'
        s += f'Treasure {r.treasure}\n'
        s += f'Time {r.time}\n\n'
        s += f'exploration cards to reveal: {c.orienteer_cards}'
        self.textEdit.setText(s)
        self.repaint()
