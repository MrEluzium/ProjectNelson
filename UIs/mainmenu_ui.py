# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainmenu.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(208, 270)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/ico/engine.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(30, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setTextFormat(QtCore.Qt.AutoText)
        self.logo.setObjectName("logo")
        self.verticalLayout_2.addWidget(self.logo)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.continue_btn = QtWidgets.QPushButton(self.centralwidget)
        self.continue_btn.setObjectName("continue_btn")
        self.verticalLayout.addWidget(self.continue_btn)
        self.newgame_btn = QtWidgets.QPushButton(self.centralwidget)
        self.newgame_btn.setObjectName("newgame_btn")
        self.verticalLayout.addWidget(self.newgame_btn)
        self.settings_btn = QtWidgets.QPushButton(self.centralwidget)
        self.settings_btn.setObjectName("settings_btn")
        self.verticalLayout.addWidget(self.settings_btn)
        self.quit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.quit_btn.setObjectName("quit_btn")
        self.verticalLayout.addWidget(self.quit_btn)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Main menu"))
        self.logo.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Times New Roman\'; font-size:16pt; font-weight:600; font-style:italic;\">PROJECT: NELSON<br/></span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-style:italic;\">ver. 1.0 dev show</span></p></body></html>"))
        self.continue_btn.setText(_translate("mainWindow", "Continue"))
        self.newgame_btn.setText(_translate("mainWindow", "New game"))
        self.settings_btn.setText(_translate("mainWindow", "Settings"))
        self.quit_btn.setText(_translate("mainWindow", "Quit"))


