# Leer el contenido del archivo de texto 'datos.txt' y almacenar sus líneas en una lista. Imprimir la cantidad de líneas que tiene el archivo y su contenido.
with open('tarea_texto.txt','r') as archivo:
    contenido = archivo.read()
    for lineas in archivo:
        print(2)
    # print(f'cantidad de lineas: {cantidad}\n')
    print(contenido)
