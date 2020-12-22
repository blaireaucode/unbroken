# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/CombatActionsWidget.ui',
# licensing of 'ui/CombatActionsWidget.ui' applies.
#
# Created: Tue Dec 22 11:04:37 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_CombatActionsWidget(object):
    def setupUi(self, CombatActionsWidget):
        CombatActionsWidget.setObjectName("CombatActionsWidget")
        CombatActionsWidget.resize(785, 481)
        self.gridLayout = QtWidgets.QGridLayout(CombatActionsWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.retranslateUi(CombatActionsWidget)
        QtCore.QMetaObject.connectSlotsByName(CombatActionsWidget)

    def retranslateUi(self, CombatActionsWidget):
        CombatActionsWidget.setWindowTitle(QtWidgets.QApplication.translate("CombatActionsWidget", "Form", None, -1))

import unbroken_rc
