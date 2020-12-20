from PySide2.QtCore import Slot, Signal, QSize
from PySide2 import QtWidgets
from .ui_EncounterWidget import Ui_EncounterWidget
from .SlidingStackedWidget import *
from core.helpers import *


class EncounterWidget(QtWidgets.QWidget, Ui_EncounterWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.game = None
        self.slidingStacked = SlidingStackedWidget()
        self.slidingStacked.setWrap(True)
        self.horizontalLayout.replaceWidget(self.label, self.slidingStacked)
        self.label.setVisible(False)
        self.label.deleteLater()
        self.image_widgets = []
        # button text
        self.previous.setText(('Previous'))  # FIXME traduction
        self.next.setText(('Next'))
        self.previous.pressed.connect(self.slot_previous)
        self.next.pressed.connect(self.slot_next)
        self.set_no_encounter()

    @Slot()
    def slot_next(self):
        self.slidingStacked.slideInNext()
        self.change_current_encounter()

    @Slot()
    def slot_previous(self):
        self.slidingStacked.slideInPrev()
        self.change_current_encounter()

    def set_game(self, g):
        self.game = g
        if not g:
            return
        self.game.phase_changed.connect(self.slot_on_phase_changed)
        self.game.character.character_changed.connect(self.slot_on_phase_changed)
        self.slot_on_phase_changed()

    def slot_on_phase_changed(self, **kwargs):
        e = self.game.encounters
        for w in self.image_widgets:
            self.slidingStacked.removeWidget(w)
        self.image_widgets.clear()
        if not e:
            self.set_no_encounter()
        else:
            self.set_encounters()
        self.repaint()

    def set_encounters(self):
        e = self.game.encounters
        s = ''
        for ee in e:
            s += f'Encounter: {ee}\n'
            self.build_widget(ee)
        for w in self.image_widgets:
            self.slidingStacked.addWidget(w)
        self.change_current_encounter()
        if len(e) < 2:
            self.previous.setVisible(False)
            self.next.setVisible(False)
        else:
            self.previous.setVisible(True)
            self.next.setVisible(True)

    def build_widget(self, encounter=False):
        l = QtWidgets.QLabel(self)
        l.setGeometry(QtCore.QRect(520, 50, 351, 461))
        l.setFrameShape(QtWidgets.QFrame.Box)
        l.setFrameShadow(QtWidgets.QFrame.Sunken)
        l.setText("")
        l.setFrameShape(QtWidgets.QFrame.NoFrame)
        s = ":/encounters/encounters/back.png"
        if encounter:
            s = ":/encounters/encounters/" + str(encounter.id) + ".png"
            l.setObjectName(encounter.name)
        l.setPixmap(QtGui.QPixmap(s))
        l.setAlignment(QtCore.Qt.AlignCenter)
        self.image_widgets.append(l)
        return l

    def change_current_encounter(self):
        i = self.slidingStacked.m_next  # not sure why 'next'
        if i >= len(self.game.encounters):
            i = 0
        e = self.game.encounters[i]
        self.label_name.setText(e.name)
        self.label_spend.setText(ff('Spend: {e.spend}'))
        self.label_gain.setText(ff('Gain: {e.gain}'))
        self.label_time.setText(ff('Time: {e.time}'))
        self.label_index.setText(ff('{i + 1}/{len(self.game.encounters)}'))
        # self.current_encounter = e
        self.repaint()

    def set_no_encounter(self):
        w = self.build_widget()
        self.slidingStacked.addWidget(w)
        s = ff('No encounters card yet')
        if self.game:
            n = n = self.game.character.orienteer_cards
            s = ff('{n} cards will be revealed')
        self.label_name.setText(s)
        self.label_spend.setText('')
        self.label_gain.setText('')
        self.label_time.setText('')
        self.label_index.setText('')
        self.previous.setVisible(False)
        self.next.setVisible(False)
