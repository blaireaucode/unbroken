# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ActionsWidget.ui',
# licensing of 'ui/ActionsWidget.ui' applies.
#
# Created: Sun Nov 29 15:53:29 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ActionsWidget(object):
    def setupUi(self, ActionsWidget):
        ActionsWidget.setObjectName("ActionsWidget")
        ActionsWidget.resize(681, 455)
        self.verticalLayout = QtWidgets.QVBoxLayout(ActionsWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.action_layout = QtWidgets.QVBoxLayout()
        self.action_layout.setObjectName("action_layout")
        self.debug1 = ActionWidget(ActionsWidget)
        self.debug1.setObjectName("debug1")
        self.action_layout.addWidget(self.debug1)
        self.debug2 = ActionWidget(ActionsWidget)
        self.debug2.setObjectName("debug2")
        self.action_layout.addWidget(self.debug2)
        self.verticalLayout.addLayout(self.action_layout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(ActionsWidget)
        QtCore.QMetaObject.connectSlotsByName(ActionsWidget)

    def retranslateUi(self, ActionsWidget):
        ActionsWidget.setWindowTitle(QtWidgets.QApplication.translate("ActionsWidget", "Form", None, -1))

from .ActionWidget import ActionWidget
import unbroken_rc
