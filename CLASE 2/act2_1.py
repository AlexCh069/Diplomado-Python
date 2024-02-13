
# creamos el archvio y le damos 3 lineas de texto
with open('datos.txt', 'w') as archivo:
    for i in range(1,4):
        archivo.write(f'{i}. Lineas de texto\n')