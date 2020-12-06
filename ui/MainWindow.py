from .ui_MainWindow import Ui_MainWindow
from .NewGameWidget import *
import gettext
import os
# import config
import configparser


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # setup ui
        self.setupUi(self)
        self.setWindowTitle("Unbroken")

        # config file
        self.config = None
        self.config_filename = '.unbroken.cfg'
        self.read_config(self.config_filename)

        # language
        self.init_language()

        # init the game
        self.game = None
        self.init_game()

        # setup ui
        self.button_new.clicked.connect(self.slot_on_new_game)
        self.button_save.clicked.connect(self.slot_on_save_game)

    def read_config(self, fn):
        self.config = configparser.ConfigParser()
        if not os.path.exists(fn):
            self.config['default'] = {'lang': 'en'}
            f = open(fn, 'w')
            self.config.write(f)
        self.config.read(fn)

    def init_language(self):
        l = self.config['default']['lang']
        lang1 = gettext.translation('messages', localedir='locales', languages=[l])
        lang1.install()

    def init_game(self):
        g = None
        if 'last_game' in self.config['default']:
            f = self.config['default']['last_game']
            self.slot_on_load_game(f)

    def set_game(self, g):
        self.game = g
        if g:
            self.button_save.setEnabled(True)
        else:
            self.button_save.setEnabled(False)
        # FIXME main stuff here
        self.widget_character.set_game(g)
        self.widget_phase.set_game(g)
        self.widget_encounter.set_game(g)
        self.widget_actions.set_game(g)

    @Slot()
    def slot_on_load_game(self, filename):
        g = Game()
        f = self.config['default']['last_game']
        if os.path.exists(f):
            g = g.load(f)
            self.set_game(g)

    @Slot()
    def slot_on_new_game(self):
        diag = NewGameWidget(self)
        r = diag.exec_()
        if r == 0:
            return
        g = diag.game
        self.set_game(g)

    @Slot()
    def slot_on_save_game(self):
        filename = 'test.json'
        self.game.save(filename)
        self.config['default']['last_game'] = filename
        with open(self.config_filename, 'w') as f:
            self.config.write(f)
