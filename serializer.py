import serial
import serial.tools.list_ports
import binascii
from time import sleep


class Serializer:

    def __init__(self):
        print("Serializing.")
        sleep(1)
        print("Serializing..")
        sleep(1)
        print("Serializing...")
        sleep(1)
        print("*Beep boop* Serialized")

        self.port = None
        self.baud_rate = 9600
        self.bytesize = 8
        self.parity = serial.PARITY_NONE
        self.stop_bits = serial

    @staticmethod
    def get_serial_port():
        ports = serial.tools.list_ports.comports()
        return ports
        # for i, port in enumerate(ports):
        #     print(f"{i}: {port.device}")
        #
        # port_index = int(input("Wybierz numer portu: "))
        # return ports[port_index].device


    def get_connection_parameters(self):
        baud_rate = int(input("Podaj baud rate: "))
        parity = input("Podaj parity bit (N/E/O): ").upper()
        data_bits = int(input("Podaj ilość data bits (5/6/7/8): "))
        stop_bits = float(input("Podaj ilość stop bits (1/1.5/2): "))
        handshaking = input("Podaj handshaking (XON/XOFF/RTSCTS/NONE): ").upper()

        parity_dict = {'N': serial.PARITY_NONE, 'E': serial.PARITY_EVEN, 'O': serial.PARITY_ODD}
        stop_bits_dict = {1: serial.STOPBITS_ONE, 1.5: serial.STOPBITS_ONE_POINT_FIVE, 2: serial.STOPBITS_TWO}
        handshaking_dict = {'XON/XOFF': serial.XON, 'RTSCTS': serial.RTSCTS, 'NONE': serial.NONE}

        return {
            'baudrate': baud_rate,
            'parity': parity_dict[parity],
            'bytesize': data_bits,
            'stopbits': stop_bits_dict[stop_bits],
            'xonxoff': handshaking == 'XON/XOFF',
            'rtscts': handshaking == 'RTSCTS',
            'dsrdtr': False  # DSR/DTR handshaking not handled in this example
        }

    def hex_to_bytes(self, hex_string):
        return binascii.unhexlify(hex_string)

    def send_frame(self, port, params, frame):
        parity_dict = {'N': serial.PARITY_NONE, 'E': serial.PARITY_EVEN, 'O': serial.PARITY_ODD}
        stop_bits_dict = {'1': serial.STOPBITS_ONE, '1.5': serial.STOPBITS_ONE_POINT_FIVE, '2': serial.STOPBITS_TWO}

        params['parity'] = parity_dict[params['parity']]
        params['stopbits'] = stop_bits_dict[params['stopbits']]

        with serial.Serial(port, **params) as ser:
            hex_frame = frame
            print(f"Połączono z {port}")
            frame_bytes = self.hex_to_bytes(hex_frame)
            ser.write(frame_bytes)

            print(f"Wysłana ramka: {frame_bytes.hex().upper()}")

            response = ser.read(32)
            print(f"Otrzymana ramka: {response.hex().upper()}")
            return response
