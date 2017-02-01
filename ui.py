# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front_end.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main_window(QtWidgets.QMainWindow):

    def __init__(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(508, 341)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 481, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.send_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.send_btn.setObjectName("send_btn")
        self.gridLayout.addWidget(self.send_btn, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 481, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 230, 481, 41))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.connect_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.connect_btn.setObjectName("connect_btn")
        self.gridLayout_2.addWidget(self.connect_btn, 0, 1, 1, 1)
        self.disconnect_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.disconnect_btn.setObjectName("disconnect_btn")
        self.gridLayout_2.addWidget(self.disconnect_btn, 0, 0, 1, 1)
        self.buad_rate = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.buad_rate.setObjectName("buad_rate")
        self.gridLayout_2.addWidget(self.buad_rate, 0, 3, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_2.addWidget(self.comboBox_3, 0, 2, 1, 1)
        self.serial_port = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.serial_port.setObjectName("serial_port")
        self.gridLayout_2.addWidget(self.serial_port, 0, 4, 1, 1)
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
        self.connect_btn.setText(_translate("main_window", "Connect"))
        self.disconnect_btn.setText(_translate("main_window", "Disconnect"))

    # Set Status Bar Message
    def set_status_bar(self,text):
        self.statusbar.showMessage(text)

    # Add tuple of Serial Port for Combo box
    def add_serial_port(self,tuple):
        self.serial_port.addItem(tuple)
        pass


if __name__== "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window(main_window)
    main_window.show()
    sys.exit(app.exec_())

