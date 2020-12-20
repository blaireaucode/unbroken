# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ChooseEncounterActionWidget.ui',
# licensing of 'ui/ChooseEncounterActionWidget.ui' applies.
#
# Created: Sun Dec 20 17:59:00 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ChooseEncounterActionWidget(object):
    def setupUi(self, ChooseEncounterActionWidget):
        ChooseEncounterActionWidget.setObjectName("ChooseEncounterActionWidget")
        ChooseEncounterActionWidget.resize(408, 90)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ChooseEncounterActionWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_text = QtWidgets.QLabel(ChooseEncounterActionWidget)
        self.label_text.setWordWrap(True)
        self.label_text.setObjectName("label_text")
        self.horizontalLayout.addWidget(self.label_text)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(ChooseEncounterActionWidget)
        QtCore.QMetaObject.connectSlotsByName(ChooseEncounterActionWidget)

    def retranslateUi(self, ChooseEncounterActionWidget):
        ChooseEncounterActionWidget.setWindowTitle(QtWidgets.QApplication.translate("ChooseEncounterActionWidget", "Form", None, -1))
        self.label_text.setText(QtWidgets.QApplication.translate("ChooseEncounterActionWidget", "Choose the card", None, -1))

import unbroken_rc
