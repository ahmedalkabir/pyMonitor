"""
    pyMonitor first Version

    Written By :Ahmed Alkabir
"""
#!/usr/bin/python3

# Library
import serial
import sys

class pyMonitor():

    #baud rate of Serial communication
    baud_rate = [4800,9600,14400,19200,28800,38400,57600,115200]

    # serial object
    __main_conn = None


    #   Constructor
    def __init__(self, port, baud_rate, byte_size=serial.EIGHTBITS, parity=serial.PARITY_NONE, stop_bit=serial.STOPBITS_ONE):

        self.__main_conn = serial.Serial(port, baud_rate, bytesize=byte_size, parity=parity, stopbits=stop_bit)

        pass

    # Close Connection of Serial Communication
    @classmethod
    def close_connection(cls):
        if cls.__main_conn is not None:
            cls.__main_conn.close()


    # Ports of Computers and it depends on os system
    @staticmethod
    def get_port():
        if sys.platform.startswith('win'):                          # For Windows Platform
            ports = ['COM%s' %(i + 1) for i in range(256)]

            win_ports = []
            for port in ports:
                try:
                    # Check if port it works if work add to results list otherwise ignore it
                    temp_port = serial.Serial(port)
                    temp_port.close()

                    win_ports.append(port)
                except (OSError, serial.SerialException):
                    pass
            # return ports
            return win_ports

        elif sys.platform.startswith('linux'):                      # For Linux Platform
            ports = ['/dev/ttyUSB%s'%(i) for i in range(256)]

            linux_ports = []
            for port in ports:
                try:
                    # Check if port it works if work add to results list otherwise ignore it
                    temp_port = serial.Serial(port)
                    temp_port.close()

                    linux_ports.append(port)
                except(OSError, serial.SerialException):
                    pass
            # return ports
            return linux_ports







def main():
    a = pyMonitor(pyMonitor.get_port()[0],pyMonitor.baud_rate[0])


main()