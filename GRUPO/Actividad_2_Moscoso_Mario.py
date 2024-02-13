
""" Cree un archivo de texto llamado 'datos.txt', almacene tres líneas de texto. Abrir luego el archivo creado con un editor de texto."""

file=open("datos.txt","w")
file.write("linea1")
file.write("\nlinea2")
file.write("\nlinea3")
file.close()

"""Lea el contenido del archivo de texto 'datos.txt'."""

# Lectura el arcivo
filelectura1=open("datos.txt","r")
print(filelectura1.read())
filelectura1.close()

"""Lea el contenido del archivo de texto 'datos.txt' línea a línea."""

# Lectura el archivo creado línea por línea 
filelectura2=open("datos.txt","r")
print(filelectura2.readlines())
filelectura2.close()

"""Leer el contenido del archivo de texto 'datos.txt' y almacenar sus líneas en una lista. Imprimir la cantidad de líneas que tiene el archivo y su contenido."""
# a una lista
filelectura3=open("datos.txt","r")
lista1 =[]
i=1
for linea in filelectura3:
    lista1.append(linea)
    i=i+1
print ("Las lineas cargadas en la lista son :",lista1)
print ("El nro de filas en el texto es:",i)
filelectura3.close()



