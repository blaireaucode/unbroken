# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/GenericActionWidget.ui',
# licensing of 'ui/GenericActionWidget.ui' applies.
#
# Created: Mon Dec 21 20:54:25 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_GenericActionWidget(object):
    def setupUi(self, GenericActionWidget):
        GenericActionWidget.setObjectName("GenericActionWidget")
        GenericActionWidget.resize(384, 83)
        self.verticalLayout = QtWidgets.QVBoxLayout(GenericActionWidget)
        self.verticalLayout.setContentsMargins(6, 0, 6, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(-1)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_do_it = QtWidgets.QPushButton(GenericActionWidget)
        self.button_do_it.setObjectName("button_do_it")
        self.horizontalLayout.addWidget(self.button_do_it)
        self.label_name = QtWidgets.QLabel(GenericActionWidget)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout.addWidget(self.label_name)
        spacerItem = QtWidgets.QSpacerItem(40, 2, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_action_type = QtWidgets.QLabel(GenericActionWidget)
        self.label_action_type.setObjectName("label_action_type")
        self.horizontalLayout.addWidget(self.label_action_type)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_text = QtWidgets.QLabel(GenericActionWidget)
        self.label_text.setWordWrap(True)
        self.label_text.setObjectName("label_text")
        self.verticalLayout.addWidget(self.label_text)
        self.line = QtWidgets.QFrame(GenericActionWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)

        self.retranslateUi(GenericActionWidget)
        QtCore.QMetaObject.connectSlotsByName(GenericActionWidget)

    def retranslateUi(self, GenericActionWidget):
        GenericActionWidget.setWindowTitle(QtWidgets.QApplication.translate("GenericActionWidget", "Form", None, -1))
        self.button_do_it.setText(QtWidgets.QApplication.translate("GenericActionWidget", "Do it", None, -1))
        self.label_name.setText(QtWidgets.QApplication.translate("GenericActionWidget", "Inspiration", None, -1))
        self.label_action_type.setText(QtWidgets.QApplication.translate("GenericActionWidget", "(General)", None, -1))
        self.label_text.setText(QtWidgets.QApplication.translate("GenericActionWidget", "After a monster\'s combat roll spend <Effort> to reduce the roll result by 1.", None, -1))

import unbroken_rc
