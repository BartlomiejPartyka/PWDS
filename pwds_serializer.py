import serial
import time
import threading
import datetime
import serial.tools.list_ports
from units import get_unit


class PWDS_Serializer:
    def __init__(self):
        self.port = '\\\\.\\COM5'
        self.baudrate = 9600
        self.bytesize = serial.EIGHTBITS
        self.stopbits = serial.STOPBITS_ONE

        self.thread = None
        self.stop_thread = False
        self.textbox = None
        self.writing_to_file = False
        self.file = None
        self.time = 1

    def send_frame(self):
        """Sends a single frame with request to get current reading from the DMM"""
        ser = serial.Serial(self.port, self.baudrate, bytesize=self.bytesize, stopbits=self.stopbits, timeout=1)
        ser.setRTS = True

        command = b'\x10\x02\x00\x00\x00\x00\x10\x03'

        # Reading response from DMM
        while not self.stop_thread:
            ser.write(command)
            response = ser.read(100)
            if len(response) > 8:
                ascii_start = 8
                ascii_end = len(response) - 3
                ascii_bytes = response[ascii_start:ascii_end]
                ascii_representation = ascii_bytes.decode('ascii')

                # Extracting the value and unit, sending to textbox and file
                match = ascii_representation.split(' ')
                if match:
                    value = float(match[1])
                    raw_unit = match[2].strip()
                    unit = get_unit(raw_unit)
                    current_time = datetime.datetime.now()
                    current_time = current_time.strftime('%d/%m/%Y %H:%M:%S')

                    self.textbox.insert("end", f"Data:  {str(current_time)}     Wartość: {str(value)} {unit}\n")
                    self.check_textbox()

                    if self.writing_to_file:
                        self.file.write(f"Data:  {str(current_time)}     Wartość: {str(value)} {unit}\n")
            time.sleep(self.time)
        ser.close()

    def start_sending(self):
        """Starts thread, starting sending frames to the DMM"""
        self.stop_thread = False
        self.thread = threading.Thread(target=self.send_frame)
        self.thread.start()

    def stop_sending(self):
        """Joins thread, stopping sending frames to the DMM"""
        self.stop_thread = True
        if self.thread is not None:
            self.thread.join()

    @staticmethod
    def get_serial_port():
        """Returns a list of available COM port objects"""
        ports = serial.tools.list_ports.comports()
        return ports

    def check_textbox(self):
        """Checks number of lines displayed in textbox, removes unnecessary old lines"""
        nol = int(self.textbox.index('end').split('.')[0]) - 1
        if nol >= 40:
            self.textbox.delete("1.0", "2.0")
