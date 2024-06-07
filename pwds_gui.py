import customtkinter as ctk
from pwds_serializer import PWDS_Serializer
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


class PWDS_GUI:
    def __init__(self):
        self.state = False
        self.writing_to_file = False
        self.serializer = PWDS_Serializer()
        self.start_button = None
        self.filepath_button = None
        self.start_file_button = None
        self.combobox = None
        self.path_label = None
        self.textbox = None
        self.f = None

    def display(self):
        root = ctk.CTk(fg_color="white")
        root.title('Projekt_PWDS')
        root.geometry("800x600")

        frame_top = ctk.CTkFrame(master=root, fg_color="white")
        frame_top.pack(side='top')
        frame_options = ctk.CTkFrame(master=root, fg_color="white")
        frame_options.pack(side='top')
        frame_text = ctk.CTkFrame(master=root, fg_color="white")
        frame_text.pack(side='top')
        title_label = ctk.CTkLabel(master=frame_top, text="Sanwa PC5000a", font=("Helvetica", 25), fg_color="white")
        title_label.grid(row=0, column=0, pady=20)
        self.start_button = ctk.CTkButton(master=frame_options, text="Start", fg_color="#E7E7E7", corner_radius=10,
                                          text_color="black",
                                          cursor="hand2", hover_color="#CACACA", command=self.start)
        self.start_button.grid(row=0, column=0, padx=10)
        self.filepath_button = ctk.CTkButton(master=frame_options, text="Wybiesz ścieżkę", fg_color="#E7E7E7",
                                        corner_radius=10,
                                        text_color="black", command=self.select_file,
                                        cursor="hand2", hover_color="#CACACA")
        self.filepath_button.grid(row=0, column=1, padx=10)
        self.start_file_button = ctk.CTkButton(master=frame_options, text="Zapisuj do pliku", fg_color="#E7E7E7",
                                          corner_radius=10, state='disabled',
                                          text_color="black", command=self.start_writing_to_file,
                                          cursor="arrow", hover_color="#CACACA")
        self.start_file_button.grid(row=0, column=2, padx=10)
        self.combobox = ctk.CTkComboBox(master=frame_options, values=['1 sekunda', '2 sekundy', '5 sekund', '10 sekund', '30 sekund',
                                                                 '1 minuta', '5 minut', '10 minut', '30 minut'],
                                   state='readonly', command=self.time_changing)
        self.combobox.set('1 sekunda')
        self.combobox.grid(row=0, column=3, padx=10)
        self.path_label = ctk.CTkLabel(master=frame_text, text='', text_color="black", fg_color="white", font=("Helvetica", 12))
        self.path_label.grid(row=0, column=0, pady=10)
        self.textbox = ctk.CTkTextbox(frame_text, width=700, height=400, border_width=2,
                                      border_color="#B7B7B7", wrap='word', font=("Helvetica", 15))
        self.textbox.grid(row=1, column=0, pady=10)
        self.serializer.textbox = self.textbox

        root.mainloop()

    def start(self):
        self.state = not self.state
        if self.state:
            if self.path_label.cget('text') != '':
                self.start_file_button.configure(state='normal')
            self.start_button.configure(text="Stop", text_color="red")
            self.serializer.start_sending()
        else:
            self.start_file_button.configure(state='disabled', cursor='arrow')
            self.start_button.configure(text="Start", text_color="black")
            self.serializer.stop_sending()

    def start_writing_to_file(self):
        self.writing_to_file = not self.writing_to_file
        if self.writing_to_file:
            self.start_file_button.configure(text="Koniec zapisu", text_color="red")
            self.filepath_button.configure(state='disabled')
            self.serializer.writing_to_file = True
            self.f = open(self.path_label.cget('text'), "w")
            self.serializer.file = self.f
        else:
            self.serializer.writing_to_file = False
            self.start_file_button.configure(text="Zapisuj do pliku", text_color="black")
            self.filepath_button.configure(state='normal')
            self.f.close()

    def time_changing(self, value):
        number, unit = value.split(' ')
        if unit == 'sekund' or unit == 'sekunda' or unit == 'sekundy':
            pass
        else:
            number = number * 60
        self.serializer.time = int(number)

    def select_file(self):
        filetypes = (
            ('*.txt', '*.txt'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        self.path_label.configure(text=filename)
        if self.state:
            self.start_file_button.configure(state='normal', cursor='hand2')
