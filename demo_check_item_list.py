# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo_check_item_list.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_item_list_dialog(object):
    def setupUi(self, item_list_dialog):
        item_list_dialog.setObjectName("item_list_dialog")
        item_list_dialog.resize(359, 517)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(item_list_dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.item_check_listWidget = QtWidgets.QListWidget(item_list_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_check_listWidget.sizePolicy().hasHeightForWidth())
        self.item_check_listWidget.setSizePolicy(sizePolicy)
        self.item_check_listWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.item_check_listWidget.setFont(font)
        self.item_check_listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.item_check_listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.item_check_listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.item_check_listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.item_check_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.item_check_listWidget.setProperty("isWrapping", False)
        self.item_check_listWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.item_check_listWidget.setObjectName("item_check_listWidget")
        self.verticalLayout.addWidget(self.item_check_listWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(item_list_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(item_list_dialog)
        self.buttonBox.accepted.connect(item_list_dialog.accept)
        self.buttonBox.rejected.connect(item_list_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(item_list_dialog)

    def retranslateUi(self, item_list_dialog):
        _translate = QtCore.QCoreApplication.translate
        item_list_dialog.setWindowTitle(_translate("item_list_dialog", "检查项目"))
        self.item_check_listWidget.setSortingEnabled(True)

