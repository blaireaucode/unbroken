# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/NewGameWidget.ui',
# licensing of 'ui/NewGameWidget.ui' applies.
#
# Created: Mon Nov 23 21:19:21 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_NewGameWidget(object):
    def setupUi(self, NewGameWidget):
        NewGameWidget.setObjectName("NewGameWidget")
        NewGameWidget.resize(907, 586)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewGameWidget)
        self.buttonBox.setGeometry(QtCore.QRect(540, 540, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_3 = QtWidgets.QLabel(NewGameWidget)
        self.label_3.setGeometry(QtCore.QRect(110, 120, 281, 251))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(NewGameWidget)
        self.label_2.setGeometry(QtCore.QRect(180, 60, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(NewGameWidget)
        self.label.setGeometry(QtCore.QRect(520, 50, 351, 461))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/character/sneak.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(NewGameWidget)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), NewGameWidget.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), NewGameWidget.reject)
        QtCore.QMetaObject.connectSlotsByName(NewGameWidget)

    def retranslateUi(self, NewGameWidget):
        NewGameWidget.setWindowTitle(QtWidgets.QApplication.translate("NewGameWidget", "Dialog", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("NewGameWidget", "Le Furtif\n"
"Le Bagarreur\n"
"Révélez +1 carte quand vous pigez une nouvelle Habilité.\n"
"Jeter un œil (Voyager): Révélez +1 carte pendant la Phase Voyager.\n"
"Juste une égratignure (Combat):\n"
"Après le jet de dé du monstre, dépensez pour réduire ce résultat de 1.", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("NewGameWidget", "Sneak", None, -1))

import unbroken_rc
import unbroken_rc
