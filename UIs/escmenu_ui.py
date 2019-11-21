# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'escmenu.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(208, 269)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/ico/engine.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(30, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.logo = QtWidgets.QLabel(Form)
        self.logo.setTextFormat(QtCore.Qt.AutoText)
        self.logo.setObjectName("logo")
        self.gridLayout.addWidget(self.logo, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.continue_btn = QtWidgets.QPushButton(Form)
        self.continue_btn.setObjectName("continue_btn")
        self.verticalLayout.addWidget(self.continue_btn)
        self.settings_btn = QtWidgets.QPushButton(Form)
        self.settings_btn.setObjectName("settings_btn")
        self.verticalLayout.addWidget(self.settings_btn)
        self.mainmenu_btn = QtWidgets.QPushButton(Form)
        self.mainmenu_btn.setObjectName("mainmenu_btn")
        self.verticalLayout.addWidget(self.mainmenu_btn)
        self.quit_btn = QtWidgets.QPushButton(Form)
        self.quit_btn.setObjectName("quit_btn")
        self.verticalLayout.addWidget(self.quit_btn)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Menu"))
        self.logo.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Times New Roman\'; font-size:14pt; font-weight:600; font-style:italic;\">Menu</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; font-style:italic;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:16pt; font-weight:600; font-style:italic;\">PROJECT: NELSON<br/></span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-style:italic;\">ver. 1.0 dev show</span></p></body></html>"))
        self.continue_btn.setText(_translate("Form", "Continue"))
        self.settings_btn.setText(_translate("Form", "Settings"))
        self.mainmenu_btn.setText(_translate("Form", "Main menu"))
        self.quit_btn.setText(_translate("Form", "Quit"))


