from .ui_MultipleActionsWidget import Ui_MultipleActionsWidget
from .GenericActionWidget import *


class MultipleActionsWidget(QtWidgets.QWidget, Ui_MultipleActionsWidget):

    def __init__(self, game, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.game = game
        self.action_widgets = []
        self.update()

    def update(self, **kwargs):
        # remove previous
        for a in self.action_widgets:
            self.action_layout.removeWidget(a)
            a.setVisible(False)
        self.action_widgets = []
        # set the new action
        actions = self.game.get_current_activities()
        for a in actions:
            wa = GenericActionWidget(self, a)
            self.action_layout.addWidget(wa)
            self.action_widgets.append(wa)
        self.repaint()
