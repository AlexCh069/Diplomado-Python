import tkinter as tk
from tkinter import ttk

# Función para mostrar el nombre y el país seleccionado
def mostrar_datos():
    nombre = entry_nombre.get()
    pais = combobox_pais.get()
    mensaje = f"Nombre: {nombre}, País: {pais}"
    estado.set(mensaje)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Registro de Persona")

# Crear una variable de control para mostrar el estado
estado = tk.StringVar()
estado.set("")

# Etiqueta y entrada para el nombre
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

# Combobox para seleccionar el país
label_pais = tk.Label(ventana, text="País:")
label_pais.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
paises = ["Argentina", "Brasil", "Chile", "Colombia", "México", "Perú"]
combobox_pais = ttk.Combobox(ventana, values=paises)
combobox_pais.grid(row=1, column=1, padx=5, pady=5)

# Botón para mostrar los datos
boton_mostrar = tk.Button(ventana, text="Mostrar", command=mostrar_datos)
boton_mostrar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Etiqueta para mostrar el estado
label_estado = tk.Label(ventana, textvariable=estado, bd=1, relief=tk.SUNKEN, anchor=tk.W)
label_estado.grid(row=3, column=0, columnspan=2, sticky=tk.W+tk.E, padx=5, pady=5)

# Bucle principal de Tkinter
ventana.mainloop()
