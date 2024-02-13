# Disponer de varios objetos de la clase Checkbutton con nombres de navegadores web. 
# En el título de la ventana mostrará todos los nombres de navegadores seleccionados.

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.window = tk.Tk()
        self.var_title = tk.StringVar
        self.var_title = "Checkbutton navegadores: "
        self.window.title(self.var_title)

        self.navegadores_web = ["Google Chrome","Mozilla Firefox","Safari","Microsoft Edge","Opera"]
        self.vars_seleccions = []


        for index,navegador in enumerate(self.navegadores_web):
            self.var_seleccion = tk.IntVar()
            self.check = tk.Checkbutton(self.window, text= navegador, variable= self.var_seleccion, command= self.change_titel)
            self.vars_seleccions.append(self.var_seleccion)     # Guardo las variables en orden de navegardor
            self.check.grid(row= index, column= 0)

        self.window.mainloop()

    def change_titel(self):
        self.var_title = "Navegadores: "

        change_names = []
        for index,vars in enumerate(self.vars_seleccions):
            if vars.get() == 1:
                change_names.append(self.navegadores_web[index])
        
        for i in change_names:
            self.var_title += f'{i} +'
            self.window.title(self.var_title)



        print(change_names)  # Para pruebas 



aplicacion = Aplicacion()
