"""Lea el contenido del archivo de texto 
'datos.txt' línea a línea."""

# Lectura el archivo creado línea por línea 
filelectura2=open("datos.txt","r")
print(filelectura2.readlines())
filelectura2.close()