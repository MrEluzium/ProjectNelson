# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gameplay.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(489, 253)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/ico/engine.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 471, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dialog_name_lb = QtWidgets.QLabel(self.layoutWidget)
        self.dialog_name_lb.setObjectName("dialog_name_lb")
        self.verticalLayout.addWidget(self.dialog_name_lb)
        self.replica_show = QtWidgets.QTextBrowser(self.layoutWidget)
        self.replica_show.setObjectName("replica_show")
        self.verticalLayout.addWidget(self.replica_show)
        self.location_lb = QtWidgets.QLabel(Form)
        self.location_lb.setGeometry(QtCore.QRect(400, 170, 77, 51))
        self.location_lb.setObjectName("location_lb")
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(120, 170, 239, 54))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.dialog_btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.dialog_btn.setObjectName("dialog_btn")
        self.gridLayout.addWidget(self.dialog_btn, 0, 0, 1, 1)
        self.battle_btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.battle_btn.setObjectName("battle_btn")
        self.gridLayout.addWidget(self.battle_btn, 0, 1, 1, 1)
        self.trade_btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.trade_btn.setObjectName("trade_btn")
        self.gridLayout.addWidget(self.trade_btn, 0, 2, 1, 1)
        self.menu_btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.menu_btn.setObjectName("menu_btn")
        self.gridLayout.addWidget(self.menu_btn, 1, 0, 1, 1)
        self.inventory_btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.inventory_btn.setObjectName("inventory_btn")
        self.gridLayout.addWidget(self.inventory_btn, 1, 1, 1, 1)
        self.next_btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.next_btn.setObjectName("next_btn")
        self.gridLayout.addWidget(self.next_btn, 1, 2, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 160, 67, 72))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lvl_lb = QtWidgets.QLabel(self.layoutWidget2)
        self.lvl_lb.setObjectName("lvl_lb")
        self.verticalLayout_2.addWidget(self.lvl_lb)
        self.exp_lb = QtWidgets.QLabel(self.layoutWidget2)
        self.exp_lb.setObjectName("exp_lb")
        self.verticalLayout_2.addWidget(self.exp_lb)
        self.hp_lb = QtWidgets.QLabel(self.layoutWidget2)
        self.hp_lb.setObjectName("hp_lb")
        self.verticalLayout_2.addWidget(self.hp_lb)
        self.money_lb = QtWidgets.QLabel(self.layoutWidget2)
        self.money_lb.setObjectName("money_lb")
        self.verticalLayout_2.addWidget(self.money_lb)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PROJECT: NELSON"))
        self.dialog_name_lb.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Джеймс</span></p></body></html>"))
        self.replica_show.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system\'; font-size:12pt; color:#000000; background-color:#ffffff;\">Я есмь Альфа и Омега, начало и конец; жаждущему дам даром от источника воды живой.</span></p></body></html>"))
        self.location_lb.setText(_translate("Form", "<html><head/><body><p align=\"right\">Location:<br/>Литл-Лэмплайт<br/>Большой зал</p></body></html>"))
        self.dialog_btn.setText(_translate("Form", "Dialoge"))
        self.battle_btn.setText(_translate("Form", "Battle"))
        self.trade_btn.setText(_translate("Form", "Trade"))
        self.menu_btn.setText(_translate("Form", "Menu"))
        self.inventory_btn.setText(_translate("Form", "Inventory"))
        self.next_btn.setText(_translate("Form", "Next"))
        self.lvl_lb.setText(_translate("Form", "LvL: 2"))
        self.exp_lb.setText(_translate("Form", "Exp: 180/250"))
        self.hp_lb.setText(_translate("Form", "HP: 100/100"))
        self.money_lb.setText(_translate("Form", "₪: 17"))


