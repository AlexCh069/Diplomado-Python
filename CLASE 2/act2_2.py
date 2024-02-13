# Lea el contenido del archivo de texto 'datos.txt'.

with open('datos.txt','r') as archivo:
    contenido = archivo.read()  # Leemos el contenido del archivo
    print(contenido)            # imprimimos el contenido del archivo
