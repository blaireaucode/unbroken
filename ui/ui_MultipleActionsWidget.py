# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MultipleActionsWidget.ui',
# licensing of 'ui/MultipleActionsWidget.ui' applies.
#
# Created: Tue Dec 22 11:04:37 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MultipleActionsWidget(object):
    def setupUi(self, MultipleActionsWidget):
        MultipleActionsWidget.setObjectName("MultipleActionsWidget")
        MultipleActionsWidget.resize(671, 463)
        self.gridLayout = QtWidgets.QGridLayout(MultipleActionsWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(MultipleActionsWidget)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 647, 439))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.action_layout = QtWidgets.QGridLayout()
        self.action_layout.setObjectName("action_layout")
        self.verticalLayout.addLayout(self.action_layout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(MultipleActionsWidget)
        QtCore.QMetaObject.connectSlotsByName(MultipleActionsWidget)

    def retranslateUi(self, MultipleActionsWidget):
        MultipleActionsWidget.setWindowTitle(QtWidgets.QApplication.translate("MultipleActionsWidget", "Form", None, -1))

import unbroken_rc
