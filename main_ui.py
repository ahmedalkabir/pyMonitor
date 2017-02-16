"""
    pyMonitor first Version

    Written By :Ahmed Alkabir
"""

#!/usr/bin/python3

from PyQt5 import  QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
from pyMonitor import pyMonitor
import ui
import _thread as thread ,queue


# Signal Implementing
class Communicate(QObject):
    recv = pyqtSignal()

#
class Ui_window(ui.Ui_main_window):

    def __init__(self,main_window):
        super().__init__(main_window)
        # Default Variable
        self.pyPort = None
        # Option of Sending Data
        self.text_option = ['No Line Ending','New Line']
        #
        self.plain_update = Communicate()
        self.plain_update.recv.connect(self.get_data)

        # Add options to UI
        # Add list of Serial Port to serial_port object of Combo Box
        self.serial_port.addItems(pyMonitor.get_port())
        # Add list of Baud rate
        self.add_baud_rate(pyMonitor.baud_rate)
        # Add Options of How Sending String
        self.status_txt.addItems(self.text_option)

        # For Stop Threads from Work
        self.worked = None

    # Add list of Baud rate to baud_rate object of Combo Box
    def add_baud_rate(self, list_baud):
        # cause value of baud rate list are integer we have
        # to include it to string in ui
        for B_list in list_baud:
            self.baud_rate.addItem(str(B_list))

    # Add list of Stop Bits (Argument is Dictionary) to Combo Box
    def add_stop_bits(self, dict):
        self.stop_bits.addItems(list(dict.keys()))

    # Add list of Parity Check
    def add_parity_check(self,dict):
        self.parity_check.addItems(list(dict.keys()))

    # Add list of Byte Size
    def add_bytesize(self,dict):
        self.bytesize.addItems(list(dict.keys()))

    # Unlock Advanced option by Check Box
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

    # Slots Function
    def btn_connect(self):
        status_message_bar = 'Connected to {} and Baud rate is {}'.format(self.serial_port.currentText(),self.baud_rate.currentText())
        # To prevent
        self.connect_btn.setEnabled(False)
        # Update StatusBar
        self.statusbar.showMessage(status_message_bar)
        # Clear Plain Text
        self.plainTextEdit.clear()

        # create pyMonitor object and connect
        try:
            self.pyPort = pyMonitor(self.serial_port.currentText(),self.baud_rate.currentText())
            # if connection Success
            if self.pyPort is not None:
                # Start New Thread that receive data from target device
                # Set Worked Flag to True
                self.worked = True
                self.receive_data()

        except Exception:
            self.statusbar.showMessage('Error Maybe Port is used')
            self.connect_btn.setEnabled(True)

    def btn_disconnect(self):

        # To Make Sure that we're connected otherwise don't do any thing

        if self.worked:
            # Sent Stop to CheckStatusQueue to Stop pyPort.receive_data and Stop
            # pyPort.receive_data thread
            self.pyPort.checkStatusQueue.put('Stop')
            # Make Worked False to Stop refresh_plain_text thread
            self.worked = False
            # Close the Connection
            self.pyPort.close_connection()
            # Return Connect Button to Normal State
            self.connect_btn.setEnabled(True)
            # Update Status Bar
            self.statusbar.showMessage('Disconnected')

    def send_data(self):
        if self.pyPort is not None:
            # Options of How Sending Data
            if self.text_option[0] == self.status_txt.currentText():
                self.pyPort.transmit_data(self.lineEdit.text().encode())
            elif self.text_option[1] == self.status_txt.currentText():
                self.pyPort.transmit_data((self.lineEdit.text()+'\n').encode())

        else:
            self.statusbar.showMessage('Please Connect Before Send Any Thing')
        # Clear it for Another Text To Send
        self.lineEdit.clear()


    def receive_data(self):
        # Start New Thread for pyPort object that can receive data and put it
        # by queue
        thread.start_new_thread(self.pyPort.receive_data,())
        # Start New thread for plain text updating data when come from devices
        thread.start_new_thread(self.refresh_plain_text,())




    # To Add Data to Plain Text
    # When queue added to pyPort.dataQueue it added
    # to received_data and emit signal
    def refresh_plain_text(self):
        while self.worked:
            try:
                self.received_data = self.pyPort.dataQueue.get()
                #update Text plain
                self.plain_update.recv.emit()
            except queue.Empty:
                pass
    # when signal emitted the plainText Update
    def get_data(self):
        self.plainTextEdit.insertPlainText(self.received_data)