# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ActionsWidget.ui',
# licensing of 'ui/ActionsWidget.ui' applies.
#
# Created: Sun Nov 29 18:29:17 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ActionsWidget(object):
    def setupUi(self, ActionsWidget):
        ActionsWidget.setObjectName("ActionsWidget")
        ActionsWidget.resize(604, 367)
        self.gridLayout = QtWidgets.QGridLayout(ActionsWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(ActionsWidget)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 580, 343))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.action_layout = QtWidgets.QVBoxLayout()
        self.action_layout.setObjectName("action_layout")
        self.debug1 = ActionWidget(self.scrollAreaWidgetContents)
        self.debug1.setObjectName("debug1")
        self.action_layout.addWidget(self.debug1)
        self.debug2 = ActionWidget(self.scrollAreaWidgetContents)
        self.debug2.setObjectName("debug2")
        self.action_layout.addWidget(self.debug2)
        self.verticalLayout.addLayout(self.action_layout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(ActionsWidget)
        QtCore.QMetaObject.connectSlotsByName(ActionsWidget)

    def retranslateUi(self, ActionsWidget):
        ActionsWidget.setWindowTitle(QtWidgets.QApplication.translate("ActionsWidget", "Form", None, -1))

from .ActionWidget import ActionWidget
import unbroken_rc
