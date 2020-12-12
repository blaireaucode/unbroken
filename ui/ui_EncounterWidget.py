# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/EncounterWidget.ui',
# licensing of 'ui/EncounterWidget.ui' applies.
#
# Created: Sat Dec 12 17:22:20 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_EncounterWidget(object):
    def setupUi(self, EncounterWidget):
        EncounterWidget.setObjectName("EncounterWidget")
        EncounterWidget.resize(777, 534)
        self.gridLayout_2 = QtWidgets.QGridLayout(EncounterWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(EncounterWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(EncounterWidget)
        QtCore.QMetaObject.connectSlotsByName(EncounterWidget)

    def retranslateUi(self, EncounterWidget):
        EncounterWidget.setWindowTitle(QtWidgets.QApplication.translate("EncounterWidget", "Form", None, -1))
        self.textEdit.setHtml(QtWidgets.QApplication.translate("EncounterWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">EncounterWidget</p></body></html>", None, -1))

