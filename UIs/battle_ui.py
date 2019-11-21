# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'battle.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(463, 347)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/ico/engine.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.opponent_state_lb = QtWidgets.QLabel(Form)
        self.opponent_state_lb.setObjectName("opponent_state_lb")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.opponent_state_lb)
        self.opponent_name_lb = QtWidgets.QLabel(Form)
        self.opponent_name_lb.setObjectName("opponent_name_lb")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.opponent_name_lb)
        self.opponent_hp_lb = QtWidgets.QLabel(Form)
        self.opponent_hp_lb.setObjectName("opponent_hp_lb")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.opponent_hp_lb)
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.action_lb = QtWidgets.QLabel(Form)
        self.action_lb.setObjectName("action_lb")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.action_lb)
        self.action_profit_lb = QtWidgets.QLabel(Form)
        self.action_profit_lb.setObjectName("action_profit_lb")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.action_profit_lb)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.weapon_attack_btn = QtWidgets.QPushButton(Form)
        self.weapon_attack_btn.setObjectName("weapon_attack_btn")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.weapon_attack_btn)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.use_spell_btn = QtWidgets.QPushButton(Form)
        self.use_spell_btn.setObjectName("use_spell_btn")
        self.horizontalLayout.addWidget(self.use_spell_btn)
        self.spell_book_btn = QtWidgets.QPushButton(Form)
        self.spell_book_btn.setEnabled(True)
        self.spell_book_btn.setObjectName("spell_book_btn")
        self.horizontalLayout.addWidget(self.spell_book_btn)
        self.formLayout.setLayout(8, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        self.try_to_run_btn = QtWidgets.QPushButton(Form)
        self.try_to_run_btn.setObjectName("try_to_run_btn")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.try_to_run_btn)
        self.hero_hp_lb = QtWidgets.QLabel(Form)
        self.hero_hp_lb.setObjectName("hero_hp_lb")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.SpanningRole, self.hero_hp_lb)
        self.hero_name_lb = QtWidgets.QLabel(Form)
        self.hero_name_lb.setObjectName("hero_name_lb")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.SpanningRole, self.hero_name_lb)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.opponent_state_lb.setText(_translate("Form", "<html><body><p align=\"center\"><span style=\" font-weight:600;\">Великий король-маг</span></p></body></html>"))
        self.opponent_name_lb.setText(_translate("Form", "<html><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Эрик Картман</span></p></body></html>"))
        self.opponent_hp_lb.setText(_translate("Form", "<html><body><p align=\"center\"><span style=\" font-size:9pt;\">HP: 148/150</span></p></body></html>"))
        self.action_lb.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">--------</span></p></body></html>"))
        self.action_profit_lb.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.weapon_attack_btn.setText(_translate("Form", "Ударить с Warrior\'s Blade  |  Damage: 2"))
        self.use_spell_btn.setText(_translate("Form", "Использовать заклинание"))
        self.spell_book_btn.setText(_translate("Form", "Книга заклинаний"))
        self.try_to_run_btn.setText(_translate("Form", "Попытаться убежать"))
        self.hero_hp_lb.setText(_translate("Form", "<html><body><p align=\"center\"><span style=\" font-size:9pt;\">HP: 98/100</span></p></body></html>"))
        self.hero_name_lb.setText(_translate("Form", "<html><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Вы</span></p></body></html>"))


