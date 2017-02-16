"""
    pyMonitor first Version

    Written By :Ahmed Alkabir
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front_end.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main_window(object):



    # constructor
    def __init__(self,main_window):
        # initialize the ui
        self.setupUi(main_window)
        # Connect Object Layout to Functions
        self.checkBox.stateChanged.connect(self.unlock_advanced_option)
        self.connect_btn.clicked.connect(self.btn_connect)
        self.send_btn.clicked.connect(self.send_data)
        self.disconnect_btn.clicked.connect(self.btn_disconnect)



    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(606, 371)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 591, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grid_1 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid_1.setContentsMargins(0, 0, 0, 0)
        self.grid_1.setObjectName("grid_1")
        self.send_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.send_btn.setObjectName("send_btn")
        self.grid_1.addWidget(self.send_btn, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.grid_1.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 591, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 247, 591, 51))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.grid_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.grid_2.setContentsMargins(0, 0, 0, 0)
        self.grid_2.setObjectName("grid_2")
        self.status_txt = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.status_txt.setObjectName("status_txt")
        self.grid_2.addWidget(self.status_txt, 0, 2, 1, 1)
        self.baud_rate = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.baud_rate.setObjectName("baud_rate")
        self.grid_2.addWidget(self.baud_rate, 0, 1, 1, 1)
        self.bytesize = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.bytesize.setEnabled(False)
        self.bytesize.setObjectName("bytesize")
        self.grid_2.addWidget(self.bytesize, 0, 3, 1, 1)
        self.serial_port = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.serial_port.setEditable(False)
        self.serial_port.setCurrentText("")
        self.serial_port.setObjectName("serial_port")
        self.grid_2.addWidget(self.serial_port, 0, 0, 1, 1)
        self.stop_bits = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.stop_bits.setEnabled(False)
        self.stop_bits.setObjectName("stop_bits")
        self.grid_2.addWidget(self.stop_bits, 0, 6, 1, 1)
        self.parity_check = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.parity_check.setEnabled(False)
        self.parity_check.setObjectName("parity_check")
        self.grid_2.addWidget(self.parity_check, 0, 5, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 300, 591, 31))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.connect_btn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.connect_btn.setObjectName("connect_btn")
        self.gridLayout.addWidget(self.connect_btn, 0, 0, 1, 1)
        self.about = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.about.setObjectName("about")
        self.gridLayout.addWidget(self.about, 0, 4, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 2, 1, 1)
        self.disconnect_btn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.disconnect_btn.setObjectName("disconnect_btn")
        self.gridLayout.addWidget(self.disconnect_btn, 0, 1, 1, 1)
        self.auto_scroll = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.auto_scroll.setObjectName("auto_scroll")
        self.gridLayout.addWidget(self.auto_scroll, 0, 3, 1, 1)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 606, 21))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "pyMonitor"))
        self.send_btn.setText(_translate("main_window", "Send"))
        self.connect_btn.setText(_translate("main_window", "Connect"))
        self.about.setText(_translate("main_window", "About"))
        self.checkBox.setText(_translate("main_window", "Customize Advance Option"))
        self.disconnect_btn.setText(_translate("main_window", "Disconnect"))
        self.auto_scroll.setText(_translate("main_window", "Auto Scroll"))