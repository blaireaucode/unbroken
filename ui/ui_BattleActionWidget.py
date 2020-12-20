# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/BattleActionWidget.ui',
# licensing of 'ui/BattleActionWidget.ui' applies.
#
# Created: Sun Dec 20 17:59:01 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_BattleActionWidget(object):
    def setupUi(self, BattleActionWidget):
        BattleActionWidget.setObjectName("BattleActionWidget")
        BattleActionWidget.resize(408, 90)
        self.horizontalLayout = QtWidgets.QHBoxLayout(BattleActionWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_text = QtWidgets.QLabel(BattleActionWidget)
        self.label_text.setWordWrap(True)
        self.label_text.setObjectName("label_text")
        self.horizontalLayout.addWidget(self.label_text)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_trick = QtWidgets.QPushButton(BattleActionWidget)
        self.button_trick.setObjectName("button_trick")
        self.verticalLayout.addWidget(self.button_trick)
        self.button_fight = QtWidgets.QPushButton(BattleActionWidget)
        self.button_fight.setObjectName("button_fight")
        self.verticalLayout.addWidget(self.button_fight)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(BattleActionWidget)
        QtCore.QMetaObject.connectSlotsByName(BattleActionWidget)

    def retranslateUi(self, BattleActionWidget):
        BattleActionWidget.setWindowTitle(QtWidgets.QApplication.translate("BattleActionWidget", "Form", None, -1))
        self.label_text.setText(QtWidgets.QApplication.translate("BattleActionWidget", "Trick ? ", None, -1))
        self.button_trick.setText(QtWidgets.QApplication.translate("BattleActionWidget", "Trick", None, -1))
        self.button_fight.setText(QtWidgets.QApplication.translate("BattleActionWidget", "Fight", None, -1))

import unbroken_rc
