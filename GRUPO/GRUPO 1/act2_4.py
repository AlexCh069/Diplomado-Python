"""Leer el contenido del archivo de texto 'datos.txt' y 
almacenar sus líneas en una lista. Imprimir la cantidad 
de líneas que tiene el archivo y su contenido."""
# a una lista
filelectura3=open("datos.txt","r")
lista1 =[]
i=0
for linea in filelectura3:
    lista1.append(linea)
    i=i+1
print ("Las lineas cargadas en la lista son :",lista1)
print ("El nro de filas en el texto es:",i)
filelectura3.close()
