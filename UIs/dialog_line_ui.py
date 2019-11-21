# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_line.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(488, 180)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.answ_one_btn = QtWidgets.QPushButton(Form)
        self.answ_one_btn.setObjectName("answ_one_btn")
        self.verticalLayout.addWidget(self.answ_one_btn)
        self.answ_three_btn = QtWidgets.QPushButton(Form)
        self.answ_three_btn.setObjectName("answ_three_btn")
        self.verticalLayout.addWidget(self.answ_three_btn)
        self.answ_two_btn = QtWidgets.QPushButton(Form)
        self.answ_two_btn.setObjectName("answ_two_btn")
        self.verticalLayout.addWidget(self.answ_two_btn)
        self.answ_four_btn = QtWidgets.QPushButton(Form)
        self.answ_four_btn.setObjectName("answ_four_btn")
        self.verticalLayout.addWidget(self.answ_four_btn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.answ_one_btn.setText(_translate("Form", "1"))
        self.answ_three_btn.setText(_translate("Form", "2"))
        self.answ_two_btn.setText(_translate("Form", "3"))
        self.answ_four_btn.setText(_translate("Form", "4"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. Ладно, ладно. Только не бейте меня! </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. Разве ты не видишь? Тебя использовали. Ты просто пешка. Ты заслуживаешь большего. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. Зачем ты это делаешь? Зачем ты служишь машине? </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4. Я хочу заметить, что ваше &quot;государство&quot; нелегитимно. У вас нет права управлять страной.</span></p></body></html>"))


