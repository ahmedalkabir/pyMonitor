"""
    pyMonitor first Version

    Written By :Ahmed Alkabir
"""
#!/usr/bin/python3

# Library
import serial
import sys,queue,time

class pyMonitor(object):

    #baud rate of Serial communication
    baud_rate = [4800,9600,14400,19200,28800,38400,57600,115200]

    # Parity Check list
    Parity = {'PARITY_NONE':serial.PARITY_NONE,'PARITY_EVEN':serial.PARITY_EVEN,'PARITY_ODD':serial.PARITY_ODD}

    # Bit Width List or ByteSize
    ByteSize = {'FIVEBITS':serial.FIVEBITS,'SIXBITS':serial.SIXBITS,'SEVENBITS':serial.SEVENBITS,'EIGHTBITS':serial.EIGHTBITS}

    # stopBits List
    stopbits = {'STOPBITS_ONE':serial.STOPBITS_ONE,'STOPBITS_ONE_POINT_FIVE':serial.STOPBITS_ONE_POINT_FIVE,'STOPBITS_TWO':serial.STOPBITS_TWO}

    # serial object
    __main_conn = None
    dataQueue = None
    checkStatusQueue = None
    out = None
    __flag_out = None

    try:
        #   Constructor
        def __init__(self, port, baud_rate, byte_size=serial.EIGHTBITS, parity=serial.PARITY_NONE, stop_bit=serial.STOPBITS_ONE):

                # initialize the connection and if anything ok open the port
                self.__main_conn = serial.Serial(port, baud_rate, bytesize=byte_size, parity=parity, stopbits=stop_bit)

                # Queue
                self.dataQueue = queue.Queue()
                self.checkStatusQueue = queue.Queue()

                # Define Variables
                self.out = ''
                self.__flag_out = True

    except serial.SerialException:
        raise serial.SerialException



    # Close Connection of Serial Communication
    def close_connection(self):
        if self.__main_conn is not None:
            del self.__main_conn

    # Get Name of Current Port
    def get_name(self):
        return self.__main_conn.name

    # Transmit Data
    def transmit_data(self,data):
        # pass data to __main_conn pySerial object write method
        self.__main_conn.write(data)

    # Receive Data from Devices
    def receive_data(self):
        # And operation with __flag_out to check if want to close this thread
        while True and self.__flag_out:
            # to store received value into out variable
            # and Make __flag_out = True
            self.out = ''
            self.__flag_out = True

            # waiting for data to receive
            while self.__main_conn.inWaiting() == 0 and self.__flag_out:
                try:
                    if self.checkStatusQueue.get_nowait() == 'Stop':
                        self.__flag_out = False
                except queue.Empty:
                    pass



            # Sleep for 0.25 second
            time.sleep(0.05)

            # receive data from the target device
            while self.__main_conn.inWaiting() > 0 and self.__flag_out:
                try:
                    self.out += self.__main_conn.read(1).decode("utf-8")
                except UnicodeDecodeError:
                    pass

            if self.__flag_out:
                # add to out variable
                self.dataQueue.put(self.out)

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

