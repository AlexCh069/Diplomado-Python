"""
Implementaremos un programa que solicite ejecutar un 'select' en 
la tabla 'articulos' y nos retorne todas sus filas.
"""
import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="bd1")
cursor1=conexion1.cursor()
cursor1.execute("select codigo, descripcion, precio from articulos")
for fila in cursor1:
    print(fila)
conexion1.close()   