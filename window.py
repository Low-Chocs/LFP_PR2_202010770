from tkinter import *
from lexical import lexical_analyzer
from semantical import semantical
from web import token_report
from web import error_report

class Window:

    def __init__(self):
        self.root = Tk()
        self.my_menu = Menu(self.root)
        self.root.config(menu = self.my_menu)
        self.root.title("LFP Proyecto Final 202010770")
        self.root.geometry("850x500")
        self.root.iconbitmap('images/liga.ico')
        self.message = "Bot: Bienvenido a La Liga Bot, ingresa un comando \n\n"
        self.lexical_analysis = lexical_analyzer()
        self.semantical_analysis = semantical()
        self.token_report = token_report()
        
    
    def frames(self):
        self.main_frame = LabelFrame(self.root, bg = "BLACK")
        self.main_frame.pack(fill="both", expand="yes")

    def labels(self):
        '''
        chat_label = Label(self.main_frame, height = 23, width = 91)
        chat_label.pack()
        chat_label.place(x = 10, y = 10)'''

    
    def buttons(self):
        self.error_log_button = Button(self.main_frame, text = "REPORTE DE ERRORES", width =  20, height = 3, bg = "BLACK", foreground = "#f4fcc8", font = (("Futura Maxi CG Clara", 8, "bold")), bd = 5, command = self.error_report_function)
        self.error_log_button.pack()
        self.error_log_button.place(x = 680, y = 10)

        self.clean_error_log_button = Button(self.main_frame, text = "LIMPIAR LOG DE ERRORES", width= 20, height=3, bg = "BLACK", foreground = "#f4fcc8", font = (("Futura Maxi CG Clara", 8, "bold")), bd = 5, command = self.clean_error_report)
        self.clean_error_log_button.pack()
        self.clean_error_log_button.place(x = 680, y = 70)

        self.token_report_button = Button(self.main_frame, text = "REPORTE DE TOKENS", width= 20, height=3, bg = "BLACK", foreground = "#f4fcc8", font = (("Futura Maxi CG Clara", 8, "bold")), bd = 5, command = self.token_report_function)
        self.token_report_button.pack()
        self.token_report_button.place(x = 680, y = 130)

        self.clean_token_log_button = Button(self.main_frame, text = "LIMPIAR LOG DE TOKENS", width= 20, height=3, bg = "BLACK", foreground = "#f4fcc8", font = (("Futura Maxi CG Clara", 8, "bold")), bd = 5, command = self.clean_token_report)
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

    #Functions of the buttons
    def send_message(self):
        self.read_box.delete('1.0', END)
        self.message += 'Tú: {}\n'.format(self.chat_box.get("1.0",END))
        text_to_analyze = self.chat_box.get("1.0",END)
        self.chat_box.delete("1.0",END)
        self.read_box.insert('1.0',self.message)
        self.lexical_analysis.analyzer(text_to_analyze)
        new_list = []
        if self.semantical_analysis.reading(self.lexical_analysis.get_temp_token_list(), self.lexical_analysis.get_error_list()) != None:
            self.message +=  'BOT: {}\n\n'.format(self.semantical_analysis.reading(self.lexical_analysis.get_temp_token_list(), self.lexical_analysis.get_error_list()))
        else:
            self.message +=  'BOT: No he logrado entender lo que me has dicho'
        self.read_box.delete("1.0",END)
        self.read_box.insert('1.0',self.message)
        self.lexical_analysis.get_error_list().extend(new_list)
            
    
    def token_report_function(self):
        self.token_report = token_report()
        print(type(self.lexical_analysis.get_token_list()))
        list = self.lexical_analysis.get_token_list()
        self.token_report.table(list)

    def error_report_function(self):
        self.error_report = error_report()
        print(type(self.lexical_analysis.get_token_list()))
        list = self.lexical_analysis.get_error_list()
        self.error_report.table(list)
    
    def clean_token_report(self):
        self.lexical_analysis.clean_token_report()
    

    def clean_error_report(self):
        self.lexical_analysis.clean_error_report()