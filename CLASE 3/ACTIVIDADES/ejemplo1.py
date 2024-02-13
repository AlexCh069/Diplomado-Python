import tkinter as tk


class aplicacion:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Aplicacion")

        self.btn_varon = tk.Button(self.window, text ="Varon",command= self.press_btn_varon)
        self.btn_varon.pack()

        self.btn_dama = tk.Button(self.window, text ="Dama", command= self.press_btn_dama)
        self.btn_dama.pack()

        self.window.mainloop()

    def press_btn_varon(self):
        self.window.title("Varon")
    
    def press_btn_dama(self):
        self.window.title("Dama")

aplicacion = aplicacion()
        