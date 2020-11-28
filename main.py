#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# osx bigsur bug -> all matplotlib needed ftm
import matplotlib
import matplotlib.pyplot as plt
import sys
from PySide2.QtWidgets import QApplication
from ui import MainWindow

matplotlib.use('TkAgg')


# export QT_MAC_WANTS_LAYER=1 ?

def main():
    app = QApplication(sys.argv)
    # g = Game()
    m = MainWindow()
    # m.set_game(g)
    m.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
