import customtkinter as ctk
from pwds_serializer import PWDS_Serializer


class PWDS_GUI:
    def __init__(self):
        self.textbox = None
        self.serializer = None
        self.start_button = None
        self.state = False

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
        self.start_button = ctk.CTkButton(master=frame_options, text="Start", fg_color="#E7E7E7", corner_radius=10, text_color="black",
                                     cursor="hand2", hover_color="#CACACA", command = self.start)
        self.start_button.grid(row=0, column=0, padx = 10)
        file_button = ctk.CTkButton(master=frame_options, text="Zapis do pliku", fg_color="#E7E7E7", corner_radius=10,
                                     text_color="black",
                                     cursor="hand2", hover_color="#CACACA")
        file_button.grid(row=0, column=1, padx = 10)
        combobox = ctk.CTkComboBox(master=frame_options, values=['1 sekunda', '5 sekund', '10 sekund', '30 sekund',
                                                                 '1 minuta', '5 minuta', '10 minuta', '30 minut'],
                                   state='readonly')
        combobox.set('1 sekunda')
        combobox.grid(row=0, column=2, padx= 10)

        self.textbox = ctk.CTkTextbox(frame_text, width = 700, height = 400, border_width=2,
                                 border_color="#B7B7B7", wrap = 'word', font = ("Helvetica", 15))
        self.textbox.grid(row =0, column=0, pady = 30)
        #self.textbox.insert("0.0", "new text to insert")

        root.mainloop()

    def start(self):
        self.serializer= PWDS_Serializer(self.textbox)
        self.state = not self.state
        if self.state:
            self.start_button.configure(text = "Stop", text_color = "red")
            self.serializer.start_sending()
        else:
            self.start_button.configure(text="Start", text_color="black")
            self.serializer.stop_sending()
