#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# osx bigsur bug -> all matplotlib needed ftm
import matplotlib
import matplotlib.pyplot as plt
import sys
from PySide2.QtWidgets import QApplication
from ui import MainWindow
import qdarkstyle
import os

matplotlib.use('TkAgg')


# export QT_MAC_WANTS_LAYER=1 ?


def main():
    app = QApplication(sys.argv)
    s = qdarkstyle.load_stylesheet(qt_api='pyside2')
    # print(s)
    # BACKGROUND
    s = s.replace('#19232D', '#1B1A17')
    app.setStyleSheet(s)
    m = MainWindow()
    m.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
