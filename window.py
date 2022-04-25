from tkinter import *
from lexical import lexical_analyzer

class Window:

    def __init__(self):
        self.root = Tk()
        self.my_menu = Menu(self.root)
        self.root.config(menu = self.my_menu)
        self.root.title("LFP Proyecto Final 202010770")
        self.root.geometry("850x500")
        self.message = "Bot: Bienvenido a La Liga Bot, ingresa un comando \n"
        self.lexical_analysis =lexical_analyzer()
        
    
    def frames(self):
        self.main_frame = LabelFrame(self.root, bg = "BLACK")
        self.main_frame.pack(fill="both", expand="yes")

    def labels(self):
        '''
        chat_label = Label(self.main_frame, height = 23, width = 91)
        chat_label.pack()
        chat_label.place(x = 10, y = 10)'''

    
    def buttons(self):
        self.error_log_button = Button(self.main_frame, text = "REPORTE DE ERRORES", width =  20, height = 3, bg = "BLACK", foreground = "#f4fcc8", font = (("Futura Maxi CG Clara", 8, "bold")), bd = 5)
        self.error_log_button.pack()
        self.error_log_button.place(x = 680, y = 10)

        self.clean_error_log_button = Button(self.main_frame, text = "LIMPIAR LOG DE ERRORES", width= 20, height=3, bg = "BLACK", foreground = "#f4fcc8", font = (("Futura Maxi CG Clara", 8, "bold")), bd = 5)
        self.clean_error_log_button.pack()
        self.clean_error_log_button.place(x = 680, y = 70)

        self.token_report_button = Button(self.main_frame, text = "REPORTE DE TOKENS", width= 20, height=3, bg = "BLACK", foreground = "#f4fcc8", font = (("Futura Maxi CG Clara", 8, "bold")), bd = 5)
        self.token_report_button.pack()
        self.token_report_button.place(x = 680, y = 130)

        self.clean_token_log_button = Button(self.main_frame, text = "LIMPIAR LOG DE TOKENS", width= 20, height=3, bg = "BLACK", foreground = "#f4fcc8", font = (("Futura Maxi CG Clara", 8, "bold")), bd = 5)
        self.clean_token_log_button.pack()
        self.clean_token_log_button.place(x = 680, y = 190)

        self.user_manual_button = Button(self.main_frame, text = "MANUAL DE USUARIO", width= 20, height=3, bg = "BLACK", foreground = "#f4fcc8", font = (("Futura Maxi CG Clara", 8, "bold")), bd = 5)
        self.user_manual_button.pack()
        self.user_manual_button.place(x = 680, y = 250)

        self.tecnic_manual_button = Button(self.main_frame, text = "MANUAL TÉCNICO", width= 20, height=3, bg = "BLACK", foreground = "#f4fcc8", font = (("Futura Maxi CG Clara", 8, "bold")), bd = 5)
        self.tecnic_manual_button.pack()
        self.tecnic_manual_button.place(x = 680, y = 310)

        self.send_button = Button(self.main_frame, text = "ENVIAR", width= 20, height=3, bg = "BLACK", foreground = "#f4fcc8", font = (("Futura Maxi CG Clara", 8, "bold")), bd = 5, command = self.send_message)
        self.send_button.pack()
        self.send_button.place(x = 680, y = 430)

    def text_box(self):
        self.read_box = Text(self.main_frame, bg = "BLACK", height = 22, width = 80, foreground ="WHITE")
        self.read_box.pack()
        self.read_box.place(x = 10, y = 10)
        self.read_box.insert('1.0',self.message)

        self.chat_box = Text(self.main_frame, bg = "BLACK", height = 3, width = 80, foreground ="WHITE")
        self.chat_box.pack()
        self.chat_box.place(x = 10, y = 430)

    def loop(self):
        self.root.mainloop()

    def send_message(self):
        self.read_box.delete('1.0', END)
        self.message += 'Tú: {}'.format(self.chat_box.get("1.0",END))
        text_to_analyze = self.chat_box.get("1.0",END)
        self.chat_box.delete("1.0",END)
        self.read_box.insert('1.0',self.message)
        self.lexical_analysis.analyzer(text_to_analyze)
        print(self.message)