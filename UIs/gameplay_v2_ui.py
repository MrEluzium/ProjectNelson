# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gameplay_v2.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(484, 457)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/ico/engine.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.dialog_name_lb = QtWidgets.QLabel(Form)
        self.dialog_name_lb.setObjectName("dialog_name_lb")
        self.verticalLayout.addWidget(self.dialog_name_lb)
        self.replica_show = QtWidgets.QTextBrowser(Form)
        self.replica_show.setAcceptRichText(True)
        self.replica_show.setObjectName("replica_show")
        self.verticalLayout.addWidget(self.replica_show)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.verticalLayout)
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.line_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.line)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.line_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.answ_one_btn = QtWidgets.QPushButton(Form)
        self.answ_one_btn.setObjectName("answ_one_btn")
        self.verticalLayout_4.addWidget(self.answ_one_btn)
        self.answ_two_btn = QtWidgets.QPushButton(Form)
        self.answ_two_btn.setObjectName("answ_two_btn")
        self.verticalLayout_4.addWidget(self.answ_two_btn)
        self.answ_three_btn = QtWidgets.QPushButton(Form)
        self.answ_three_btn.setObjectName("answ_three_btn")
        self.verticalLayout_4.addWidget(self.answ_three_btn)
        self.answ_four_btn = QtWidgets.QPushButton(Form)
        self.answ_four_btn.setObjectName("answ_four_btn")
        self.verticalLayout_4.addWidget(self.answ_four_btn)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.answers_show = QtWidgets.QTextBrowser(Form)
        self.answers_show.setObjectName("answers_show")
        self.horizontalLayout.addWidget(self.answers_show)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.hp_lb = QtWidgets.QLabel(Form)
        self.hp_lb.setObjectName("hp_lb")
        self.verticalLayout_2.addWidget(self.hp_lb)
        self.money_lb = QtWidgets.QLabel(Form)
        self.money_lb.setObjectName("money_lb")
        self.verticalLayout_2.addWidget(self.money_lb)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_2.addWidget(self.line_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.next_btn = QtWidgets.QPushButton(Form)
        self.next_btn.setMinimumSize(QtCore.QSize(269, 23))
        self.next_btn.setObjectName("next_btn")
        self.verticalLayout_3.addWidget(self.next_btn)
        self.inventory_btn = QtWidgets.QPushButton(Form)
        self.inventory_btn.setMinimumSize(QtCore.QSize(269, 23))
        self.inventory_btn.setObjectName("inventory_btn")
        self.verticalLayout_3.addWidget(self.inventory_btn)
        self.menu_btn = QtWidgets.QPushButton(Form)
        self.menu_btn.setMinimumSize(QtCore.QSize(269, 23))
        self.menu_btn.setObjectName("menu_btn")
        self.verticalLayout_3.addWidget(self.menu_btn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_2.addWidget(self.line_5)
        self.location_lb = QtWidgets.QLabel(Form)
        self.location_lb.setObjectName("location_lb")
        self.horizontalLayout_2.addWidget(self.location_lb)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PROJECT: NELSON"))
        self.dialog_name_lb.setText(_translate("Form", "<html><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Джеймс</span></p></body></html>"))
        self.replica_show.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system\'; font-size:12pt; color:#000000; background-color:#ffffff;\">Я есмь Альфа и Омега, начало и конец; жаждущему дам даром от источника воды живой.</span></p></body></html>"))
        self.answ_one_btn.setText(_translate("Form", "1"))
        self.answ_two_btn.setText(_translate("Form", "2"))
        self.answ_three_btn.setText(_translate("Form", "3"))
        self.answ_four_btn.setText(_translate("Form", "4"))
        self.answers_show.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. Ладно, ладно. Только не бейте меня! </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. Разве ты не видишь? Тебя использовали. Ты просто пешка. Ты заслуживаешь большего. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. Зачем ты это делаешь? Зачем ты служишь машине? </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4. Я хочу заметить, что ваше &quot;государство&quot; нелегитимно. У вас нет права управлять страной.</span></p></body></html>"))
        self.hp_lb.setText(_translate("Form", "<html><body><p align=\"center\">HP: 100/100</p></body></html>"))
        self.money_lb.setText(_translate("Form", "<html><p align=\"center\">₪: 0</p></body></html>"))
        self.next_btn.setText(_translate("Form", "Next"))
        self.inventory_btn.setText(_translate("Form", "Inventory"))
        self.menu_btn.setText(_translate("Form", "Menu"))
        self.location_lb.setText(_translate("Form", "<html><head/><body><p align=\"center\">Location<br/>Литл-Лэмплайт<br/>Большой зал</p></body></html>"))


