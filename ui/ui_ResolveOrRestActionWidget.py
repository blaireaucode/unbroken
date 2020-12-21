# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ResolveOrRestActionWidget.ui',
# licensing of 'ui/ResolveOrRestActionWidget.ui' applies.
#
# Created: Mon Dec 21 15:51:19 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ResolveOrRestActionWidget(object):
    def setupUi(self, ResolveOrRestActionWidget):
        ResolveOrRestActionWidget.setObjectName("ResolveOrRestActionWidget")
        ResolveOrRestActionWidget.resize(408, 90)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ResolveOrRestActionWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_text = QtWidgets.QLabel(ResolveOrRestActionWidget)
        self.label_text.setWordWrap(True)
        self.label_text.setObjectName("label_text")
        self.horizontalLayout.addWidget(self.label_text)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_resolve = QtWidgets.QPushButton(ResolveOrRestActionWidget)
        self.button_resolve.setObjectName("button_resolve")
        self.verticalLayout.addWidget(self.button_resolve)
        self.button_rest = QtWidgets.QPushButton(ResolveOrRestActionWidget)
        self.button_rest.setObjectName("button_rest")
        self.verticalLayout.addWidget(self.button_rest)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(ResolveOrRestActionWidget)
        QtCore.QMetaObject.connectSlotsByName(ResolveOrRestActionWidget)

    def retranslateUi(self, ResolveOrRestActionWidget):
        ResolveOrRestActionWidget.setWindowTitle(QtWidgets.QApplication.translate("ResolveOrRestActionWidget", "Form", None, -1))
        self.label_text.setText(QtWidgets.QApplication.translate("ResolveOrRestActionWidget", "Resolve the encounter ?", None, -1))
        self.button_resolve.setText(QtWidgets.QApplication.translate("ResolveOrRestActionWidget", "Resolve", None, -1))
        self.button_rest.setText(QtWidgets.QApplication.translate("ResolveOrRestActionWidget", "Rest", None, -1))

import unbroken_rc
