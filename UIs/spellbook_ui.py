# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spellbook.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(229, 348)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/ico/engine.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.spells_table = QtWidgets.QTableWidget(Form)
        self.spells_table.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.spells_table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spells_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.spells_table.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.spells_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.spells_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.spells_table.setObjectName("spells_table")
        self.spells_table.setColumnCount(2)
        self.spells_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.spells_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.spells_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.spells_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.spells_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.spells_table.setItem(0, 1, item)
        self.spells_table.horizontalHeader().setDefaultSectionSize(95)
        self.spells_table.horizontalHeader().setMinimumSectionSize(95)
        self.verticalLayout.addWidget(self.spells_table)
        self.selected_lb = QtWidgets.QLabel(Form)
        self.selected_lb.setObjectName("selected_lb")
        self.verticalLayout.addWidget(self.selected_lb)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Spellbook"))
        item = self.spells_table.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.spells_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.spells_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        __sortingEnabled = self.spells_table.isSortingEnabled()
        self.spells_table.setSortingEnabled(False)
        item = self.spells_table.item(0, 0)
        item.setText(_translate("Form", "4"))
        item = self.spells_table.item(0, 1)
        item.setText(_translate("Form", "5"))
        self.spells_table.setSortingEnabled(__sortingEnabled)
        self.selected_lb.setText(_translate("Form", "<html><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Selected: Fireball</span></p></body></html>"))


