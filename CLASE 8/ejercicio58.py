import sqlite3

conexion=sqlite3.connect("bd1.db")
precio=float(input("Ingrese un precio:"))
cursor=conexion.execute("select descripcion from articulo where precio<?", (precio, ))
filas=cursor.fetchall()
if len(filas)>0:
    for fila in filas:
        print(fila)
else:
    print("No existen artículo con un precio menor al ingresado.")
conexion.close()