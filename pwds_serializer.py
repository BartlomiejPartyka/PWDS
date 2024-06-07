import serial
import time
import threading
import datetime


class PWDS_Serializer:
    def __init__(self):
        # self.port = '\\\\.\\COM6'
        # self.baudrate = 9600
        # self.bytesize = serial.EIGHTBITS
        # self.stopbits = serial.STOPBITS_ONE

        self.thread = None
        self.stop_thread = False
        self.textbox = None
        self.writing_to_file = False
        self.file = None
        self.time = 1

    def send_frame(self):
        # ser = serial.Serial(self.port, self.baudrate, bytesize=self.bytesize, stopbits=self.stopbits, timeout=1)
        # ser.setRTS = True

        command = b'\x10\x02\x00\x00\x00\x00\x10\x03'

        while not self.stop_thread:
            # ser.write(command)
            # response = ser.read(100)
            response = 'wywal te linijkeee po odkomentowaniu koduuuu'
            if len(response) > 8:
                # ascii_start = 8
                # ascii_end = len(response) - 3
                # ascii_bytes = response[ascii_start:ascii_end]
                # ascii_representation = ascii_bytes.decode('ascii')

                current_time = datetime.datetime.now()
                current_time = current_time.strftime('%d/%m/%Y %H:%M:%S')
                self.textbox.insert("end", "Data:  " + str(current_time) + "     Wartość: \n" ) #ascii_representation + "\n")
                if self.writing_to_file:
                    self.file.write("Data:  " + str(current_time) + "     Wartość: \n")
            time.sleep(self.time)

        #ser.close()

    def start_sending(self):
        self.stop_thread = False
        self.thread = threading.Thread(target=self.send_frame)
        self.thread.start()

    def stop_sending(self):
        self.stop_thread = True
        if self.thread is not None:
            self.thread.join()




