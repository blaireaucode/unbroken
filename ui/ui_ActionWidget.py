# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ActionWidget.ui',
# licensing of 'ui/ActionWidget.ui' applies.
#
# Created: Sat Dec  5 11:58:20 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ActionWidget(object):
    def setupUi(self, ActionWidget):
        ActionWidget.setObjectName("ActionWidget")
        ActionWidget.resize(384, 83)
        self.verticalLayout = QtWidgets.QVBoxLayout(ActionWidget)
        self.verticalLayout.setContentsMargins(6, 0, 6, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(-1)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_do_it = QtWidgets.QPushButton(ActionWidget)
        self.button_do_it.setObjectName("button_do_it")
        self.horizontalLayout.addWidget(self.button_do_it)
        self.label_name = QtWidgets.QLabel(ActionWidget)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout.addWidget(self.label_name)
        spacerItem = QtWidgets.QSpacerItem(40, 2, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_action_type = QtWidgets.QLabel(ActionWidget)
        self.label_action_type.setObjectName("label_action_type")
        self.horizontalLayout.addWidget(self.label_action_type)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_text = QtWidgets.QLabel(ActionWidget)
        self.label_text.setWordWrap(True)
        self.label_text.setObjectName("label_text")
        self.verticalLayout.addWidget(self.label_text)
        self.line = QtWidgets.QFrame(ActionWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)

        self.retranslateUi(ActionWidget)
        QtCore.QMetaObject.connectSlotsByName(ActionWidget)

    def retranslateUi(self, ActionWidget):
        ActionWidget.setWindowTitle(QtWidgets.QApplication.translate("ActionWidget", "Form", None, -1))
        self.button_do_it.setText(QtWidgets.QApplication.translate("ActionWidget", "Do it", None, -1))
        self.label_name.setText(QtWidgets.QApplication.translate("ActionWidget", "Inspiration", None, -1))
        self.label_action_type.setText(QtWidgets.QApplication.translate("ActionWidget", "(General)", None, -1))
        self.label_text.setText(QtWidgets.QApplication.translate("ActionWidget", "After a monster\'s combat roll spend <Effort> to reduce the roll result by 1.", None, -1))

import unbroken_rc
