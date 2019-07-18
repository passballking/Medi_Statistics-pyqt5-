# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo_company_list.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_company_list(object):
    def setupUi(self, company_list):
        company_list.setObjectName("company_list")
        company_list.resize(411, 369)
        company_list.setToolTipDuration(0)
        self.verticalLayout = QtWidgets.QVBoxLayout(company_list)
        self.verticalLayout.setObjectName("verticalLayout")
        self.company_list_widget = QtWidgets.QListWidget(company_list)
        self.company_list_widget.setObjectName("company_list_widget")
        self.verticalLayout.addWidget(self.company_list_widget)

        self.retranslateUi(company_list)
        QtCore.QMetaObject.connectSlotsByName(company_list)

    def retranslateUi(self, company_list):
        _translate = QtCore.QCoreApplication.translate
        company_list.setWindowTitle(_translate("company_list", "公司列表-双击选定公司"))
        self.company_list_widget.setSortingEnabled(True)

