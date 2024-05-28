from tkinter import *
from serializer import Serializer


COLORS = {
    'White': '#FFFFFF',
    'Light grey': '#C0C0C0',
    'Grey': '#808080',
    'Dark grey': '#404040',
    'Black': '#000000',
}


class MainGUI(Tk):

    def __init__(self):
        super().__init__()
        self.serializer = Serializer()

        self.title("The Serializer alpha-0.9")
        self.geometry("750x750")
        self.configure(background=COLORS['White'])

        self.ports = self.serializer.get_serial_port()

        self.baud_rate = IntVar(value=9600)
        self.bytesize = IntVar(value=8)
        self.parity = StringVar(value='None')
        self.stopbits = StringVar(value='1')
        self.port = StringVar(value='')
        self.handshake = StringVar(value='NONE')

        self.baud_rate_frame = Frame(master=self, width=100, height=250, bg=COLORS['Light grey'], borderwidth=0)
        Label(self.baud_rate_frame, text="Baud Rate", bg=COLORS['Light grey']).pack()
        Radiobutton(self.baud_rate_frame, text='600', variable=self.baud_rate, value=600, bg=COLORS['Light grey'],
                    borderwidth=0).pack()
        Radiobutton(self.baud_rate_frame, text='1200', variable=self.baud_rate, value=1200, bg=COLORS['Light grey'],
                    borderwidth=0).pack()
        Radiobutton(self.baud_rate_frame, text='2400', variable=self.baud_rate, value=2400, bg=COLORS['Light grey'],
                    borderwidth=0).pack()
        Radiobutton(self.baud_rate_frame, text="4800", variable=self.baud_rate, value=4800, bg=COLORS['Light grey'],
                    borderwidth=0).pack()
        Radiobutton(self.baud_rate_frame, text="9600", variable=self.baud_rate, value=9600, bg=COLORS['Light grey'],
                    borderwidth=0).pack()
        self.baud_rate_frame.grid(row=0, column=0)

        self.stopbits_frame = Frame(master=self, width=100, height=250, bg=COLORS['Light grey'], borderwidth=0)
        Label(self.stopbits_frame, text="# of stopbits", bg=COLORS['Light grey']).pack()
        Radiobutton(self.stopbits_frame, text='1', variable=self.stopbits, value='1', bg=COLORS['Light grey'],
                    borderwidth=0).pack()
        Radiobutton(self.stopbits_frame, text='1.5', variable=self.stopbits, value='1.5', bg=COLORS['Light grey'],
                    borderwidth=0).pack()
        Radiobutton(self.stopbits_frame, text='2', variable=self.stopbits, value='2', bg=COLORS['Light grey'],
                    borderwidth=0).pack()
        self.stopbits_frame.grid(row=0, column=1)

        self.parity_frame = Frame(master=self, width=100, height=250, bg=COLORS['Light grey'], borderwidth=0)
        Label(self.parity_frame, text="Parity", bg=COLORS['Light grey']).pack()
        Radiobutton(self.parity_frame, text='None', variable=self.parity, value='N', bg=COLORS['Light grey'],
                    borderwidth=0).pack()
        Radiobutton(self.parity_frame, text='Odd', variable=self.parity, value='O', bg=COLORS['Light grey'],
                    borderwidth=0).pack()
        Radiobutton(self.parity_frame, text='Even', variable=self.parity, value='E', bg=COLORS['Light grey'],
                    borderwidth=0).pack()
        self.parity_frame.grid(row=0, column=2)

        self.bytesize_frame = Frame(master=self, width=100, height=250, bg=COLORS['Light grey'], borderwidth=0)
        Label(self.bytesize_frame, text="Byte size", bg=COLORS['Light grey']).pack()
        Radiobutton(self.bytesize_frame, text='5', variable=self.bytesize, value=5, bg=COLORS['Light grey'],
                    borderwidth=0).pack()
        Radiobutton(self.bytesize_frame, text='6', variable=self.bytesize, value=6, bg=COLORS['Light grey'],
                    borderwidth=0).pack()
        Radiobutton(self.bytesize_frame, text="7", variable=self.bytesize, value=7, bg=COLORS['Light grey'],
                    borderwidth=0).pack()
        Radiobutton(self.bytesize_frame, text="8", variable=self.bytesize, value=8, bg=COLORS['Light grey'],
                    borderwidth=0).pack()
        self.bytesize_frame.grid(row=0, column=3)

        self.handshake_frame = Frame(master=self, width=100, height=250, bg=COLORS['Light grey'], borderwidth=0)
        Label(self.handshake_frame, text="Handshake", bg=COLORS['Light grey']).pack()
        Radiobutton(self.handshake_frame, text='XON/XOFF', variable=self.handshake, value='XON/XOFF', bg=COLORS['Light grey'],
                    borderwidth=0).pack()
        Radiobutton(self.handshake_frame, text='RTSCTS', variable=self.handshake, value='RTSCTS', bg=COLORS['Light grey'],
                    borderwidth=0).pack()
        Radiobutton(self.handshake_frame, text='NONE', variable=self.handshake, value='NONE', bg=COLORS['Light grey'],
                    borderwidth=0).pack()
        self.handshake_frame.grid(row=0, column=4)

        self.ports_frame = Frame(master=self, width=100, height=250, bg=COLORS['Light grey'], borderwidth=0)
        Label(self.ports_frame, text="Ports", bg=COLORS['Light grey']).pack()
        for i, port in enumerate(self.ports):
            Radiobutton(self.ports_frame, text=port.device, variable=self.port, value=port.device,
                        bg=COLORS['Light grey'], borderwidth=0).pack()
        self.refresh_ports_btn = Button(master=self.ports_frame, text="Refresh ports", borderwidth=0,
                                        bg=COLORS['Light grey'], command=self.refresh_ports)
        self.refresh_ports_btn.pack()
        self.ports_frame.grid(row=0, column=5)

        self.frame_editor = Text(self, bg=COLORS['White'])
        self.frame_editor.grid(row=1, column=0, columnspan=5)

        self.send_btn = Button(self, bg=COLORS['Light grey'], command=self.send_frame, text='Send')
        self.send_btn.grid(row=1, column=5)

        self.frame_disp = Text(self, bg=COLORS['Grey'], state='disabled')
        self.frame_disp.grid(row=2, column=0, columnspan=6)

    def refresh_ports(self):
        for w in self.ports_frame.winfo_children():
            w.destroy()
        self.ports = self.serializer.get_serial_port()
        Label(self.ports_frame, text="Ports", bg=COLORS['Light grey']).pack()
        for i, port in enumerate(self.ports):
            Radiobutton(self.ports_frame, text=port.device, variable=self.port, value=port.device,
                        bg=COLORS['Light grey'], borderwidth=0).pack()
        self.refresh_ports_btn = Button(master=self.ports_frame, text="Refresh ports", borderwidth=0,
                                        bg=COLORS['Light grey'], command=self.refresh_ports)
        self.refresh_ports_btn.pack()

    def send_frame(self):
        frame_dict = {
            'baudrate': self.baud_rate.get(),
            'parity': self.parity.get(),
            'bytesize': self.bytesize.get(),
            'stopbits': self.stopbits.get(),
            'xonxoff': False,
            'rtscts': False,
            'dsrdtr': False # DSR/DTR handshaking not handled in this example
        }
        port = self.port.get()
        frame = self.frame_editor.get("1.0", "end-1c")

        response = self.serializer.send_frame(port, frame_dict, frame)
        self.frame_disp.configure(state='normal')
        self.frame_disp.insert('end', f'{response}\n')
        self.frame_disp.configure(state='disabled')
        self.frame_editor.delete("1.0", END)
