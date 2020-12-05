# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/TravelDecisionWidget.ui',
# licensing of 'ui/TravelDecisionWidget.ui' applies.
#
# Created: Sat Dec  5 11:58:21 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_TravelDecisionWidget(object):
    def setupUi(self, TravelDecisionWidget):
        TravelDecisionWidget.setObjectName("TravelDecisionWidget")
        TravelDecisionWidget.resize(408, 90)
        self.horizontalLayout = QtWidgets.QHBoxLayout(TravelDecisionWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_text = QtWidgets.QLabel(TravelDecisionWidget)
        self.label_text.setWordWrap(True)
        self.label_text.setObjectName("label_text")
        self.horizontalLayout.addWidget(self.label_text)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_combat = QtWidgets.QPushButton(TravelDecisionWidget)
        self.button_combat.setObjectName("button_combat")
        self.verticalLayout.addWidget(self.button_combat)
        self.button_exploration = QtWidgets.QPushButton(TravelDecisionWidget)
        self.button_exploration.setObjectName("button_exploration")
        self.verticalLayout.addWidget(self.button_exploration)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(TravelDecisionWidget)
        QtCore.QMetaObject.connectSlotsByName(TravelDecisionWidget)

    def retranslateUi(self, TravelDecisionWidget):
        TravelDecisionWidget.setWindowTitle(QtWidgets.QApplication.translate("TravelDecisionWidget", "Form", None, -1))
        self.label_text.setText(QtWidgets.QApplication.translate("TravelDecisionWidget", "Are you ready to encounter the monster?", None, -1))
        self.button_combat.setText(QtWidgets.QApplication.translate("TravelDecisionWidget", "Yes! Start the combat ...", None, -1))
        self.button_exploration.setText(QtWidgets.QApplication.translate("TravelDecisionWidget", "Not yet ... Continue Exploration", None, -1))

import unbroken_rc
