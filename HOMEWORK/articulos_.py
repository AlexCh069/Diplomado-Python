import mysql.connector

class Articulos:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost", 
                                              user="root", 
                                              passwd="", 
                                              database="bd1")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into artículos(descripcion, precio) values (%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select descripcion, precio from artículos where codigo=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select codigo, descripcion, precio from artículos"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
    
    def baja(self,datos):

        cone=self.abrir()
        cursor=cone.cursor()

        sql="delete  from artículos where codigo=%s"

        cursor.execute(sql, datos)
        cone.commit()

        return cursor.rowcount # retornamos la cantidad de filas borradas
    

    def modificacion(self, datos):

        cone=self.abrir()
        cursor=cone.cursor()
        
        sql="update artículos set descripcion=%s, precio=%s where codigo=%s"
        
        cursor.execute(sql, datos)
        cone.commit()
        
        return cursor.rowcount # retornamos la cantidad de filas modificadas