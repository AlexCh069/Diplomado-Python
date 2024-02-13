""" Cree un archivo de texto llamado 'datos.txt', almacene 
tres líneas de texto. Abrir luego el archivo creado con un 
editor de texto."""

file=open("datos.txt","w")
file.write("linea1")
file.write("\nlinea2")
file.write("\nlinea3")
file.close()
