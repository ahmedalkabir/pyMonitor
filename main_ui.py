#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets
import ui

class Ui_window(ui.Ui_main_window):


    # Add list of Serial Port to serial_port object of Combo Box
    def add_serial_port(self, list_serial):
        # Add it
        self.serial_port.addItems(list_serial)

    # Add list of Baud rate to baud_rate object of Combo Box
    def add_baud_rate(self, list_baud):
        # cause value of baud rate list are integer we have
        # to include it to string in ui
        for list in list_baud:
            self.baud_rate.addItem(str(list))

    # Add list of Stop Bits (Argument is Dictionary) to Combo Box
    def add_stop_bits(self, dict):
        self.stop_bits.addItems(list(dict.keys()))

    # Unlcok Advanced option by Check Box
    def unlock_advanced_option(self):

        # Make it all Enabled
        if self.checkBox.isChecked() is not False:
            self.stop_bits.setEnabled(True)
            self.parity_check.setEnabled(True)
            self.bytesize.setEnabled(True)
        # if unchecked disable it all
        elif self.checkBox.isChecked() is not True:
            self.stop_bits.setEnabled(False)
            self.parity_check.setEnabled(False)
            self.bytesize.setEnabled(False)