# Disponer un Listbox con una serie de nombres de frutas. 
# Permitir la selección de varias frutas. Cuando se presiona un botón 
# recuperar todas las frutas seleccionadas y mostrarlas en una etiqueta.

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Frutas")

        self.frutas = ["Manzana", "Plátano", "Naranja", "Uva", "Pera", "Piña"]

        self.listbox = tk.Listbox(self.window, selectmode= tk.MULTIPLE)
        self.listbox.grid(row= 0, column= 0)

        for fruta in self.frutas:
            self.listbox.insert(tk.END, fruta)

        self.btn_rec = tk.Button(self.window, text= "Recuperar", command= self.print_fut)
        self.btn_rec.grid(row= 1, column= 0)

        self.lbl_frutas = tk.Label(self.window, text= "Selecciones: ")
        self.lbl_frutas.grid(row= 2, column= 0)

        self.window.mainloop()
    
    def print_fut(self):
        seleccions = self.listbox.curselection()
        print_fut = ""
        for index in seleccions:
            print_fut += f'{self.listbox.get(index)}, '
        
        self.lbl_frutas.configure(text = print_fut)

aplicacion = Aplicacion()

