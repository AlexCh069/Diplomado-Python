import sqlite3

conexion=sqlite3.connect("BD3.db")
try:
    conexion.execute("""create table articulos (
                              codigo integer primary key autoincrement,
                              descripcion text,
                              precio real
                        )""")
    print("se creo la tabla articulos")                        
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")                    
conexion.close()

# NOTA: EL CONECTOR DE SQLITE, EN CASO DE NO ENCONTRAR LA BASE DE DATOS, LA PROCEDE A CREAR
# ASPECTOS A INVESTIGAR: 
#   - COMO CONECTARSE A UNA BASE DE DATOS QUE ESTA EN UNA RUTA DIFERENTE AL ARCHIVO FUENTE
