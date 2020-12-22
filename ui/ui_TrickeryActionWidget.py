# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/TrickeryActionWidget.ui',
# licensing of 'ui/TrickeryActionWidget.ui' applies.
#
# Created: Mon Dec 21 20:54:28 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_TrickeryActionWidget(object):
    def setupUi(self, TrickeryActionWidget):
        TrickeryActionWidget.setObjectName("TrickeryActionWidget")
        TrickeryActionWidget.resize(408, 90)
        self.horizontalLayout = QtWidgets.QHBoxLayout(TrickeryActionWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_text = QtWidgets.QLabel(TrickeryActionWidget)
        self.label_text.setWordWrap(True)
        self.label_text.setObjectName("label_text")
        self.horizontalLayout.addWidget(self.label_text)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_trick = QtWidgets.QPushButton(TrickeryActionWidget)
        self.button_trick.setObjectName("button_trick")
        self.verticalLayout.addWidget(self.button_trick)
        self.button_fight = QtWidgets.QPushButton(TrickeryActionWidget)
        self.button_fight.setObjectName("button_fight")
        self.verticalLayout.addWidget(self.button_fight)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(TrickeryActionWidget)
        QtCore.QMetaObject.connectSlotsByName(TrickeryActionWidget)

    def retranslateUi(self, TrickeryActionWidget):
        TrickeryActionWidget.setWindowTitle(QtWidgets.QApplication.translate("TrickeryActionWidget", "Form", None, -1))
        self.label_text.setText(QtWidgets.QApplication.translate("TrickeryActionWidget", "Trick ? ", None, -1))
        self.button_trick.setText(QtWidgets.QApplication.translate("TrickeryActionWidget", "Trick", None, -1))
        self.button_fight.setText(QtWidgets.QApplication.translate("TrickeryActionWidget", "Fight", None, -1))

import unbroken_rc
