import tkinter as tk
from tkinter import messagebox

# Función para cambiar el tamaño de la ventana
def cambiar_tamano():
    try:
        ancho = int(entry_ancho.get())
        alto = int(entry_alto.get())
        ventana.geometry(f"{ancho}x{alto}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos para el ancho y el alto.")

# Función para salir del programa
def salir():
    ventana.destroy()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Control de Tamaño")

# Crear dos controles Entry para ingresar el ancho y el alto
label_ancho = tk.Label(ventana, text="Ancho:")
label_ancho.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
entry_ancho = tk.Entry(ventana)
entry_ancho.grid(row=0, column=1, padx=5, pady=5)

label_alto = tk.Label(ventana, text="Alto:")
label_alto.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
entry_alto = tk.Entry(ventana)
entry_alto.grid(row=1, column=1, padx=5, pady=5)

# Crear un menú
menu_principal = tk.Menu(ventana)
ventana.config(menu=menu_principal)

# Opción para cambiar el tamaño de la ventana
menu_tamano = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Tamaño de Ventana", menu=menu_tamano)
menu_tamano.add_command(label="Cambiar tamaño", command=cambiar_tamano)

# Opción para salir del programa
menu_principal.add_command(label="Salir", command=salir)

# Bucle principal de Tkinter
ventana.mainloop()
