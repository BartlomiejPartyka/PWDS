import customtkinter as ctk


class PWDS_GUI:
    def __init__(self):
        self.combobox = None
        self.serializer = None

    def set_serializer(self, serializer):
        self.serializer = serializer

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
        start_button = ctk.CTkButton(master=frame_options, text="Start", fg_color="#E7E7E7", corner_radius=10, text_color="black",
                                     cursor="hand2", hover_color="#CACACA", command=self.serializer.send_frame)
        start_button.grid(row=0, column=0, padx=10)
        file_button = ctk.CTkButton(master=frame_options, text="Zapis do pliku", fg_color="#E7E7E7", corner_radius=10,
                                    text_color="black",cursor="hand2", hover_color="#CACACA")
        file_button.grid(row=0, column=1, padx=10)

        def combobox_callback(choice):
            print("combobox dropdown clicked:", choice)

        self.combobox = ctk.CTkComboBox(master=frame_options, values=['1 sekunda', '5 sekund', '10 sekund', '30 sekund',
                                                                 '1 minuta', '5 minuta', '10 minuta', '30 minut'],
                                   command=combobox_callback)
        self.combobox.grid(row=0, column=2, padx=10)

        root.mainloop()

    def get_combobox_value(self):
        value = self.combobox.get()
        return self.convert_to_seconds(value)

    def convert_to_seconds(self, value):
        mapping = {
            '1 sekunda': 1,
            '5 sekund': 5,
            '10 sekund': 10,
            '30 sekund': 30,
            '1 minuta': 60,
            '5 minut': 5 * 60,
            '10 minut': 10 * 60,
            '30 minut': 30 * 60
        }
        return mapping.get(value, 1)

