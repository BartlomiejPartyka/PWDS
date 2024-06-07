import serial
import time


class PWDS_Serializer:
    def __init__(self):
        self.port = '\\\\.\\COM6'
        self.baudrate = 9600
        self.bytesize = serial.EIGHTBITS
        self.stopbits = serial.STOPBITS_ONE

        self.send_frame()

    def send_frame(self):
        ser = serial.Serial(self.port, self.baudrate, bytesize=self.bytesize, stopbits=self.stopbits, timeout=1)
        ser.setRTS = True

        command = b'\x10\x02\x00\x00\x00\x00\x10\x03'

        while True:
            ser.write(command)
            response = ser.read(100)

            ascii_start = 8
            ascii_end = len(response)-2
            ascii_bytes = response[ascii_start:ascii_end]
            ascii_representation = ascii_bytes.decode('ascii')
            print("Received:", ascii_representation)

            time.sleep(1)

    def stop_program(self):
        ser = serial.Serial(self.port, self.baudrate, bytesize=self.bytesize, stopbits=self.stopbits, timeout=1)
        ser.close()




