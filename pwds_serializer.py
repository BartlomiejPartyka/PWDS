import serial
import time


class Serializer:
    def __init__(self):
        self.port = '\\\\.\\COM6'
        self.baudrate = 9600
        self.bytesize = serial.EIGHTBITS
        self.stopbits = serial.STOPBITS_ONE

        ser = serial.Serial(self.port, self.baudrate, bytesize=self.bytesize, stopbits=self.stopbits, timeout=1)
        ser.setRTS = True

        command = b'\x10\x02\x00\x00\x00\x00\x10\x03'
        ser.write(command)
        time.sleep(2)

        response = ser.read(100)

        print(response)

        ser.close()




