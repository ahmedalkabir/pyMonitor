# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front_end.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(508, 367)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 481, 41))
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
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 481, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 230, 481, 51))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.grid_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.grid_2.setContentsMargins(0, 0, 0, 0)
        self.grid_2.setObjectName("grid_2")
        self.status_txt = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.status_txt.setObjectName("status_txt")
        self.grid_2.addWidget(self.status_txt, 1, 2, 1, 1)
        self.baud_rate = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.baud_rate.setObjectName("baud_rate")
        self.grid_2.addWidget(self.baud_rate, 1, 1, 1, 1)
        self.bytesize = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.bytesize.setEnabled(False)
        self.bytesize.setObjectName("bytesize")
        self.grid_2.addWidget(self.bytesize, 1, 3, 1, 1)
        self.serial_port = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.serial_port.setEditable(False)
        self.serial_port.setCurrentText("")
        self.serial_port.setObjectName("serial_port")
        self.grid_2.addWidget(self.serial_port, 1, 0, 1, 1)
        self.stop_bits = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.stop_bits.setEnabled(False)
        self.stop_bits.setObjectName("stop_bits")
        self.grid_2.addWidget(self.stop_bits, 1, 6, 1, 1)
        self.parity_check = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.parity_check.setEnabled(False)
        self.parity_check.setObjectName("parity_check")
        self.grid_2.addWidget(self.parity_check, 1, 5, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox.setObjectName("checkBox")
        self.grid_2.addWidget(self.checkBox, 0, 3, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 290, 481, 31))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.disconnect_btn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.disconnect_btn.setObjectName("disconnect_btn")
        self.gridLayout.addWidget(self.disconnect_btn, 0, 1, 1, 1)
        self.connect_btn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.connect_btn.setObjectName("connect_btn")
        self.gridLayout.addWidget(self.connect_btn, 0, 0, 1, 1)
        self.about = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.about.setObjectName("about")
        self.gridLayout.addWidget(self.about, 0, 3, 1, 1)
        self.gridLayoutWidget.raise_()
        self.verticalLayoutWidget.raise_()
        self.gridLayoutWidget_2.raise_()
        self.gridLayoutWidget_3.raise_()
        self.serial_port.raise_()
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 508, 21))
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
        self.checkBox.setText(_translate("main_window", "Customize Advanced Option"))
        self.disconnect_btn.setText(_translate("main_window", "Disconnect"))
        self.connect_btn.setText(_translate("main_window", "Connect"))
        self.about.setText(_translate("main_window", "About"))

    # Add list of Serial Port to serial_port object of Combo Box
    def add_serial_port(self,list_serial):
        #Add it
        self.serial_port.addItems(list_serial)

    # Add list of Baud rate to baud_rate object of Combo Box
    def add_baud_rate(self,list_baud):
        # cause value of baud rate list are integer we have
        # to include it to string in ui
        for list in list_baud:
            self.baud_rate.addItem(str(list))
