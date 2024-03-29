"""
Desarrollar una aplicación visual con la librería tkinter que permita 
implementar los algoritmos de carga de artículos, 
consulta por código y listado completo.
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import articulos_

import db_funciones as funt

class FormularioArticulos:
    def __init__(self):
        self.articulo1=articulos_.Articulos()
        # _______________________________________________________________
        self.ventana1=tk.Tk()
        self.ventana1.title("Mantenimiento de artículos")
        #________________________________________________________________
        self.cuaderno1 = ttk.Notebook(self.ventana1)        
        self.carga_articulos()
        self.consulta_por_codigo()
        self.listado_completo()
        self.borrado()
        self.modificar()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def carga_articulos(self):

        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de artículos")

        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Artículo")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe1, text="Descripción:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        self.descripcioncarga=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe1, text="Precio:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)

        self.preciocarga=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciocarga)
        self.entryprecio.grid(column=1, row=1, padx=4, pady=4)
        
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    def agregar(self):
        descrip= self.descripcioncarga.get() 
        price = self.preciocarga.get()

        funt.run(descrip, price)        # Cambio en la funcion

        mb.showinfo("Información", "Los datos fueron cargados")
        self.descripcioncarga.set("")   # Borrado de variable
        self.preciocarga.set("")        # Borrado de variable

    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")

        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Artículo")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe2, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        self.codigo=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe2, text="Descripción:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)

        self.descripcion=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe2, textvariable=self.descripcion, state="readonly")
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)

        self.label3=ttk.Label(self.labelframe2, text="Precio:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)

        self.precio=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe2, textvariable=self.precio, state="readonly")
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        dato = self.codigo.get()     # Obtengo el valor de la variable self.codigo
        
        respuesta = funt.view_cod(dato)

        if respuesta != None:
            self.descripcion.set(respuesta[0])
            self.precio.set(respuesta[1])
        else:
            self.descripcion.set('')        # Borramos lo mostrado
            self.precio.set('')             # Borramos lo mostrado
            mb.showinfo("Información", "No existe un artículo con dicho código")



    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")

        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Artículo")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)

        self.boton1=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)

        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):

        respuesta= funt.view_all()
        self.scrolledtext1.delete("1.0", tk.END)   


        for articulo in respuesta:
            self.scrolledtext1.insert(tk.END, "código:"+str(articulo.codigo)+
                                              "\ndescripción:"+articulo.descripcion+
                                              "\nprecio:"+str(articulo.precio)+"\n\n")

    def borrado(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrado de artículos")

        self.labelframe4=ttk.LabelFrame(self.pagina4, text="Artículo")        
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe4, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        self.codigoborra=tk.StringVar()
        self.entryborra=ttk.Entry(self.labelframe4, textvariable=self.codigoborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe4, text="Borrar", command=self.borrar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
        cod =( self.codigoborra.get())
        articulo_delet = funt.delete_articulo(cod)

        if articulo_delet:
            mb.showinfo("Información", "Se borró el artículo con dicho código")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def modificar(self):
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Modificar artículo")

        self.labelframe5=ttk.LabelFrame(self.pagina5, text="Artículo")
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe5, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        self.codigomod=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe5, textvariable=self.codigomod)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe5, text="Descripción:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)

        self.descripcionmod=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe5, textvariable=self.descripcionmod)
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)

        self.label3=ttk.Label(self.labelframe5, text="Precio:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)

        self.preciomod=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe5, textvariable=self.preciomod)
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)
        
        self.boton1=ttk.Button(self.labelframe5, text="Consultar", command=self.consultar_mod)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)
        self.boton2=ttk.Button(self.labelframe5, text="Modificar", command=self.modifica)
        self.boton2.grid(column=1, row=4, padx=4, pady=4)

    def modifica(self):

        respuesta = funt.modify_articulos(int(self.codigomod.get()), 
                                          self.descripcionmod.get(),
                                          float(self.preciomod.get()))
        
        if respuesta:
            mb.showinfo("Información", "Se modificó el artículo")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def consultar_mod(self):
        dato = self.codigomod.get()     # Obtengo el valor de la variable self.codigo
        
        respuesta = funt.view_cod(dato)

        if respuesta != None:
            self.descripcionmod.set(respuesta[0])
            self.preciomod.set(respuesta[1])
        else:
            self.descripcionmod.set('')        # Borramos lo mostrado
            self.preciomod.set('')             # Borramos lo mostrado
            mb.showinfo("Información", "No existe un artículo con dicho código")


aplicacion1=FormularioArticulos()