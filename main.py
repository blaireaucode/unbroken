#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# osx bigsur bug -> all matplotlib needed ftm
import matplotlib
import sys
from PySide2.QtWidgets import QApplication, QLabel
from ui import MainWindow
from core import Game
import matplotlib.pyplot as plt
import gettext
import config
import os

matplotlib.use('TkAgg')


# export QT_MAC_WANTS_LAYER=1 ?

def main():
    # Language
    filename = '.unbroken.cfg'
    if not os.path.exists(filename):
        f = open(filename, 'w+')
        f.write("lang = 'en'")
    with open('.unbroken.cfg') as f:
        cfg = config.Config(f)
        print(cfg)
    l = cfg['lang']
    lang1 = gettext.translation('messages', localedir='locales', languages=[l])
    lang1.install()

    app = QApplication(sys.argv)
    g = Game()
    m = MainWindow()
    m.set_game(g)
    m.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
