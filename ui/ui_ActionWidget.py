# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ActionWidget.ui',
# licensing of 'ui/ActionWidget.ui' applies.
#
# Created: Tue Dec 22 11:04:37 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ActionWidget(object):
    def setupUi(self, ActionWidget):
        ActionWidget.setObjectName("ActionWidget")
        ActionWidget.resize(671, 463)
        self.gridLayout = QtWidgets.QGridLayout(ActionWidget)
        self.gridLayout.setObjectName("gridLayout")

        self.retranslateUi(ActionWidget)
        QtCore.QMetaObject.connectSlotsByName(ActionWidget)

    def retranslateUi(self, ActionWidget):
        ActionWidget.setWindowTitle(QtWidgets.QApplication.translate("ActionWidget", "Form", None, -1))

import unbroken_rc
