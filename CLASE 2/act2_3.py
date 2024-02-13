# Lea el contenido del archivo de texto 'datos.txt' línea a línea.
with open('tarea_texto.txt','r') as archivo:
    for linea in archivo:   # Leemos linea por linea el contenido del archivo
        print(linea)