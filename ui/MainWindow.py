from PySide2 import QtWidgets
from .ui_MainWindow import Ui_MainWindow
from core import Game
from PySide2.QtCore import Slot, QCoreApplication
from PySide2.QtWidgets import QAction
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QGridLayout, QWidget, QFileDialog, QMessageBox
from .NewGameWidget import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Unbroken")

        # start new game
        self.button_new.clicked.connect(self.slot_on_new_game)

    def set_game(self, g):
        print('set game', g)
        self.character.set_game(g)

    @Slot()
    def slot_on_new_game(self):
        print('okok')
        # dialog: name, difficulty + random
        # return: charcter
        diag = NewGameWidget(self) ### FIXME set the Game
        diag.show()
        print('after dialog')
        # FIXME check if cancel or not,
