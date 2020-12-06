# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/TravelDecisionActionWidget.ui',
# licensing of 'ui/TravelDecisionActionWidget.ui' applies.
#
# Created: Sat Dec  5 18:38:26 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_TravelDecisionActionWidget(object):
    def setupUi(self, TravelDecisionActionWidget):
        TravelDecisionActionWidget.setObjectName("TravelDecisionActionWidget")
        TravelDecisionActionWidget.resize(408, 90)
        self.horizontalLayout = QtWidgets.QHBoxLayout(TravelDecisionActionWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_text = QtWidgets.QLabel(TravelDecisionActionWidget)
        self.label_text.setWordWrap(True)
        self.label_text.setObjectName("label_text")
        self.horizontalLayout.addWidget(self.label_text)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_combat = QtWidgets.QPushButton(TravelDecisionActionWidget)
        self.button_combat.setObjectName("button_combat")
        self.verticalLayout.addWidget(self.button_combat)
        self.button_exploration = QtWidgets.QPushButton(TravelDecisionActionWidget)
        self.button_exploration.setObjectName("button_exploration")
        self.verticalLayout.addWidget(self.button_exploration)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(TravelDecisionActionWidget)
        QtCore.QMetaObject.connectSlotsByName(TravelDecisionActionWidget)

    def retranslateUi(self, TravelDecisionActionWidget):
        TravelDecisionActionWidget.setWindowTitle(QtWidgets.QApplication.translate("TravelDecisionActionWidget", "Form", None, -1))
        self.label_text.setText(QtWidgets.QApplication.translate("TravelDecisionActionWidget", "Are you ready to encounter the monster?", None, -1))
        self.button_combat.setText(QtWidgets.QApplication.translate("TravelDecisionActionWidget", "Yes! Start the combat ...", None, -1))
        self.button_exploration.setText(QtWidgets.QApplication.translate("TravelDecisionActionWidget", "Not yet ... Explore!", None, -1))

import unbroken_rc
