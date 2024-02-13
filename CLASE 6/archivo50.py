"""Las otras dos actividades fundamentales que podemos hacer con una tabla 
es borrar filas y modificar datos.
Desarrollaremos un pequeño programa que borre el artículo cuyo código sea 
el 1 y modifique el precio del artículo cuyo código sea 3.
"""
import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="bd1")
cursor1=conexion1.cursor()
cursor1.execute("delete from articulos where codigo=2")
cursor1.execute("update articulos set precio=60 where codigo=3")
conexion1.commit()
cursor1.execute("select codigo, descripcion, precio from articulos")
for fila in cursor1:
    print(fila)
conexion1.close()  


