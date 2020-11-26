# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/NewGameWidget.ui',
# licensing of 'ui/NewGameWidget.ui' applies.
#
# Created: Thu Nov 26 20:16:44 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_NewGameWidget(object):
    def setupUi(self, NewGameWidget):
        NewGameWidget.setObjectName("NewGameWidget")
        NewGameWidget.resize(635, 547)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(NewGameWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(NewGameWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(NewGameWidget)
        self.label_3.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previous = QtWidgets.QPushButton(NewGameWidget)
        self.previous.setObjectName("previous")
        self.horizontalLayout.addWidget(self.previous)
        self.next = QtWidgets.QPushButton(NewGameWidget)
        self.next.setObjectName("next")
        self.horizontalLayout.addWidget(self.next)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(NewGameWidget)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/character/sneak.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewGameWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(NewGameWidget)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), NewGameWidget.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), NewGameWidget.reject)
        QtCore.QMetaObject.connectSlotsByName(NewGameWidget)

    def retranslateUi(self, NewGameWidget):
        NewGameWidget.setWindowTitle(QtWidgets.QApplication.translate("NewGameWidget", "Dialog", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("NewGameWidget", "Sneak", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("NewGameWidget", "Le Furtif\n"
"Le Bagarreur\n"
"Révélez +1 carte quand vous pigez une nouvelle Habilité.\n"
"Jeter un œil (Voyager): Révélez +1 carte pendant la Phase Voyager.\n"
"Juste une égratignure (Combat):\n"
"Après le jet de dé du monstre, dépensez pour réduire ce résultat de 1.", None, -1))
        self.previous.setText(QtWidgets.QApplication.translate("NewGameWidget", "PushButton", None, -1))
        self.next.setText(QtWidgets.QApplication.translate("NewGameWidget", "PushButton", None, -1))

import unbroken_rc
import unbroken_rc
