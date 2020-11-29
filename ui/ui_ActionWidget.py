# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ActionWidget.ui',
# licensing of 'ui/ActionWidget.ui' applies.
#
# Created: Sun Nov 29 15:53:28 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ActionWidget(object):
    def setupUi(self, ActionWidget):
        ActionWidget.setObjectName("ActionWidget")
        ActionWidget.resize(292, 74)
        self.verticalLayout = QtWidgets.QVBoxLayout(ActionWidget)
        self.verticalLayout.setContentsMargins(2, 0, 2, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_doit = QtWidgets.QPushButton(ActionWidget)
        self.button_doit.setObjectName("button_doit")
        self.horizontalLayout.addWidget(self.button_doit)
        self.label_name = QtWidgets.QLabel(ActionWidget)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout.addWidget(self.label_name)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_action_type = QtWidgets.QLabel(ActionWidget)
        self.label_action_type.setObjectName("label_action_type")
        self.horizontalLayout.addWidget(self.label_action_type)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_text = QtWidgets.QLabel(ActionWidget)
        self.label_text.setWordWrap(True)
        self.label_text.setObjectName("label_text")
        self.verticalLayout.addWidget(self.label_text)

        self.retranslateUi(ActionWidget)
        QtCore.QMetaObject.connectSlotsByName(ActionWidget)

    def retranslateUi(self, ActionWidget):
        ActionWidget.setWindowTitle(QtWidgets.QApplication.translate("ActionWidget", "Form", None, -1))
        self.button_doit.setText(QtWidgets.QApplication.translate("ActionWidget", "Do it", None, -1))
        self.label_name.setText(QtWidgets.QApplication.translate("ActionWidget", "Inspiration", None, -1))
        self.label_action_type.setText(QtWidgets.QApplication.translate("ActionWidget", "(General)", None, -1))
        self.label_text.setText(QtWidgets.QApplication.translate("ActionWidget", "After a monster\'s combat roll spend <Effort> to reduce the roll result by 1.", None, -1))

import unbroken_rc
