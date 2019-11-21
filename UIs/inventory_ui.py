# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inventory.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(554, 433)
        Form.setMinimumSize(QtCore.QSize(554, 433))
        Form.setMaximumSize(QtCore.QSize(554, 433))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/ico/engine.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.inventory_tabs = QtWidgets.QTabWidget(Form)
        self.inventory_tabs.setGeometry(QtCore.QRect(0, 0, 331, 431))
        self.inventory_tabs.setElideMode(QtCore.Qt.ElideNone)
        self.inventory_tabs.setObjectName("inventory_tabs")
        self.main_tab = QtWidgets.QWidget()
        self.main_tab.setObjectName("main_tab")
        self.main_table = QtWidgets.QTableWidget(self.main_tab)
        self.main_table.setGeometry(QtCore.QRect(0, 0, 321, 401))
        self.main_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.main_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.main_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.main_table.setObjectName("main_table")
        self.main_table.setColumnCount(0)
        self.main_table.setRowCount(0)
        self.inventory_tabs.addTab(self.main_tab, "")
        self.weapon_tab = QtWidgets.QWidget()
        self.weapon_tab.setObjectName("weapon_tab")
        self.weapon_table = QtWidgets.QTableWidget(self.weapon_tab)
        self.weapon_table.setGeometry(QtCore.QRect(0, 0, 321, 401))
        self.weapon_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.weapon_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.weapon_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.weapon_table.setObjectName("weapon_table")
        self.weapon_table.setColumnCount(0)
        self.weapon_table.setRowCount(0)
        self.inventory_tabs.addTab(self.weapon_tab, "")
        self.armor_tab = QtWidgets.QWidget()
        self.armor_tab.setObjectName("armor_tab")
        self.armor_table = QtWidgets.QTableWidget(self.armor_tab)
        self.armor_table.setGeometry(QtCore.QRect(0, 0, 321, 401))
        self.armor_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.armor_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.armor_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.armor_table.setObjectName("armor_table")
        self.armor_table.setColumnCount(0)
        self.armor_table.setRowCount(0)
        self.inventory_tabs.addTab(self.armor_tab, "")
        self.spellbook_tab = QtWidgets.QWidget()
        self.spellbook_tab.setObjectName("spellbook_tab")
        self.spellbook_table = QtWidgets.QTableWidget(self.spellbook_tab)
        self.spellbook_table.setGeometry(QtCore.QRect(0, 0, 321, 401))
        self.spellbook_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.spellbook_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.spellbook_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.spellbook_table.setObjectName("spellbook_table")
        self.spellbook_table.setColumnCount(2)
        self.spellbook_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.spellbook_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.spellbook_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.spellbook_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.spellbook_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.spellbook_table.setItem(0, 1, item)
        self.spellbook_table.horizontalHeader().setDefaultSectionSize(152)
        self.spellbook_table.horizontalHeader().setMinimumSectionSize(152)
        self.inventory_tabs.addTab(self.spellbook_tab, "")
        self.money_lb = QtWidgets.QLabel(Form)
        self.money_lb.setGeometry(QtCore.QRect(230, 0, 61, 21))
        self.money_lb.setObjectName("money_lb")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(340, 260, 201, 123))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lb_static_selected = QtWidgets.QLabel(self.layoutWidget)
        self.lb_static_selected.setObjectName("lb_static_selected")
        self.verticalLayout.addWidget(self.lb_static_selected)
        self.selected_weapon_lb = QtWidgets.QLabel(self.layoutWidget)
        self.selected_weapon_lb.setObjectName("selected_weapon_lb")
        self.verticalLayout.addWidget(self.selected_weapon_lb)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.selected_armor_lb = QtWidgets.QLabel(self.layoutWidget)
        self.selected_armor_lb.setObjectName("selected_armor_lb")
        self.verticalLayout.addWidget(self.selected_armor_lb)
        self.line_4 = QtWidgets.QFrame(self.layoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(330, 100, 221, 72))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.item_lb = QtWidgets.QLabel(self.layoutWidget_2)
        self.item_lb.setObjectName("item_lb")
        self.verticalLayout_3.addWidget(self.item_lb)
        self.item_stat_lb = QtWidgets.QLabel(self.layoutWidget_2)
        self.item_stat_lb.setObjectName("item_stat_lb")
        self.verticalLayout_3.addWidget(self.item_stat_lb)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.select_btn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.select_btn.setObjectName("select_btn")
        self.horizontalLayout.addWidget(self.select_btn)
        self.delete_btn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout.addWidget(self.delete_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.done_btn = QtWidgets.QPushButton(Form)
        self.done_btn.setGeometry(QtCore.QRect(340, 400, 201, 23))
        self.done_btn.setObjectName("done_btn")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(340, 260, 61, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(480, 260, 61, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(339, 267, 4, 114))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setGeometry(QtCore.QRect(539, 267, 4, 114))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.armor_deleted_table = QtWidgets.QTableWidget(Form)
        self.armor_deleted_table.setGeometry(QtCore.QRect(560, 140, 261, 141))
        self.armor_deleted_table.setObjectName("armor_deleted_table")
        self.armor_deleted_table.setColumnCount(0)
        self.armor_deleted_table.setRowCount(0)
        self.weapon_deleted_table = QtWidgets.QTableWidget(Form)
        self.weapon_deleted_table.setGeometry(QtCore.QRect(560, 0, 261, 131))
        self.weapon_deleted_table.setObjectName("weapon_deleted_table")
        self.weapon_deleted_table.setColumnCount(0)
        self.weapon_deleted_table.setRowCount(0)
        self.weapon_selected_table = QtWidgets.QTableWidget(Form)
        self.weapon_selected_table.setGeometry(QtCore.QRect(560, 290, 261, 61))
        self.weapon_selected_table.setObjectName("weapon_selected_table")
        self.weapon_selected_table.setColumnCount(0)
        self.weapon_selected_table.setRowCount(0)
        self.armor_selected_table = QtWidgets.QTableWidget(Form)
        self.armor_selected_table.setGeometry(QtCore.QRect(560, 360, 261, 61))
        self.armor_selected_table.setObjectName("armor_selected_table")
        self.armor_selected_table.setColumnCount(0)
        self.armor_selected_table.setRowCount(0)

        self.retranslateUi(Form)
        self.inventory_tabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Inventory"))
        self.inventory_tabs.setTabText(self.inventory_tabs.indexOf(self.main_tab), _translate("Form", "Main"))
        self.inventory_tabs.setTabText(self.inventory_tabs.indexOf(self.weapon_tab), _translate("Form", "Weapon"))
        self.inventory_tabs.setTabText(self.inventory_tabs.indexOf(self.armor_tab), _translate("Form", "Armor"))
        item = self.spellbook_table.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.spellbook_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "New Column"))
        item = self.spellbook_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "b"))
        __sortingEnabled = self.spellbook_table.isSortingEnabled()
        self.spellbook_table.setSortingEnabled(False)
        item = self.spellbook_table.item(0, 0)
        item.setText(_translate("Form", "abc"))
        item = self.spellbook_table.item(0, 1)
        item.setText(_translate("Form", "dll"))
        self.spellbook_table.setSortingEnabled(__sortingEnabled)
        self.inventory_tabs.setTabText(self.inventory_tabs.indexOf(self.spellbook_tab), _translate("Form", "Spellbook"))
        self.money_lb.setText(_translate("Form", "<html><body><p align=\"right\"><span style=\" font-size:9pt;\">₪: 17</span></p></body></html>"))
        self.lb_static_selected.setText(_translate("Form", "<html><head/><body><p align=\"center\">Selected items</p></body></html>"))
        self.selected_weapon_lb.setText(_translate("Form", "<html><head/><body><p align=\"center\">| Weapon |<br/><b>Noob Super Hammer<br/>12 damage</b></p></body></html>"))
        self.selected_armor_lb.setText(_translate("Form", "<html><head/><body><p align=\"center\">| Armor |<br/><b>SWAT Armor<br/>7 protection</b></p></body></html>"))
        self.item_lb.setText(_translate("Form", "<html><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Choose item</span></p></body></html>"))
        self.item_stat_lb.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">-</span></p></body></html>"))
        self.select_btn.setText(_translate("Form", "Select"))
        self.delete_btn.setText(_translate("Form", "Delete"))
        self.done_btn.setText(_translate("Form", "Done"))

