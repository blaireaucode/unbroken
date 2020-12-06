# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/NewGameWidget.ui',
# licensing of 'ui/NewGameWidget.ui' applies.
#
# Created: Sun Dec  6 21:50:39 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_NewGameWidget(object):
    def setupUi(self, NewGameWidget):
        NewGameWidget.setObjectName("NewGameWidget")
        NewGameWidget.resize(690, 577)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(NewGameWidget)
        self.verticalLayout_3.setContentsMargins(12, 12, -1, 12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_name = QtWidgets.QLabel(NewGameWidget)
        font = QtGui.QFont()
        font.setFamily("Chalkboard")
        font.setPointSize(31)
        self.label_name.setFont(font)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.verticalLayout.addWidget(self.label_name)
        self.label_class_type = QtWidgets.QLabel(NewGameWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_class_type.setFont(font)
        self.label_class_type.setScaledContents(False)
        self.label_class_type.setAlignment(QtCore.Qt.AlignCenter)
        self.label_class_type.setObjectName("label_class_type")
        self.verticalLayout.addWidget(self.label_class_type)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_ability = QtWidgets.QLabel(NewGameWidget)
        self.label_ability.setMinimumSize(QtCore.QSize(350, 0))
        self.label_ability.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_ability.setFont(font)
        self.label_ability.setWordWrap(True)
        self.label_ability.setObjectName("label_ability")
        self.verticalLayout.addWidget(self.label_ability)
        spacerItem2 = QtWidgets.QSpacerItem(20, 181, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(NewGameWidget)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/character/maeel.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previous = QtWidgets.QPushButton(NewGameWidget)
        self.previous.setObjectName("previous")
        self.horizontalLayout.addWidget(self.previous)
        self.next = QtWidgets.QPushButton(NewGameWidget)
        self.next.setObjectName("next")
        self.horizontalLayout.addWidget(self.next)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label_index = QtWidgets.QLabel(NewGameWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_index.setFont(font)
        self.label_index.setLineWidth(1)
        self.label_index.setAlignment(QtCore.Qt.AlignCenter)
        self.label_index.setObjectName("label_index")
        self.verticalLayout_2.addWidget(self.label_index)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewGameWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(NewGameWidget)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), NewGameWidget.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), NewGameWidget.reject)
        QtCore.QMetaObject.connectSlotsByName(NewGameWidget)

    def retranslateUi(self, NewGameWidget):
        NewGameWidget.setWindowTitle(QtWidgets.QApplication.translate("NewGameWidget", "Dialog", None, -1))
        self.label_name.setText(QtWidgets.QApplication.translate("NewGameWidget", "Mae\'l", None, -1))
        self.label_class_type.setText(QtWidgets.QApplication.translate("NewGameWidget", "Sneak", None, -1))
        self.label_ability.setText(QtWidgets.QApplication.translate("NewGameWidget", "Le Furtif\n"
"Le Bagarreur\n"
"Révélez +1 carte quand vous pigez une nouvelle Habilité.\n"
"Jeter un œil (Voyager): Révélez +1 carte pendant la Phase Voyager.\n"
"Juste une égratignure (Combat):\n"
"Après le jet de dé du monstre, dépensez pour réduire ce résultat de 1.", None, -1))
        self.previous.setText(QtWidgets.QApplication.translate("NewGameWidget", "previous", None, -1))
        self.next.setText(QtWidgets.QApplication.translate("NewGameWidget", "next", None, -1))
        self.label_index.setText(QtWidgets.QApplication.translate("NewGameWidget", "2/8", None, -1))

import unbroken_rc
