import db_sqlite
from db_articulos import Articulos

def run(descrip: str, price: float):     # Carga de datos

    # Autoincremento de codigo
    registros = db_sqlite.session.query(Articulos).all()
    cod = int(registros[-1].codigo) + 1

    # Aderencia de nuevos datos
    articulo_add = Articulos(codigo= cod, descripcion= descrip, precio= price)

    db_sqlite.session.add(articulo_add)
    db_sqlite.session.commit()

def view_cod(cod: int): # Encontramos dato por codigo
    
    registro = db_sqlite.session.query(Articulos).filter_by(codigo=cod).first()
    if registro != None:
        return [registro.descripcion, registro.precio]
    
    else:
        return None

def view_all(): # Obtener todos los registros de la tabla Articulos
    registros = db_sqlite.session.query(Articulos).all()

    # Iterar sobre los registros para imprimirlos (extra para prueba)
    # for articulo in registros:
    #     print(articulo.codigo, articulo.descripcion, articulo.precio)

    return registros

def delete_articulo(cod: str): # Borrar articulos por codigo

    dato = db_sqlite.session.query(Articulos).filter_by(codigo=cod).first()

    if dato != None:
        db_sqlite.session.query(Articulos).filter_by(codigo = cod).delete() # Borramos el dato
        db_sqlite.session.commit()  # Confirmar el borrado
        db_sqlite.session.close()   # Cerramos la conexion con la db
        return True
    
    else:
        return False

def modify_articulos(cod: int, descrip: str, price: float):  # Modificar registro por codigo (no cambiamos codigo)
    # Consultar el registro con un código específico
    articulo = db_sqlite.session.query(Articulos).filter_by(codigo = cod).first()    # Buscamos el dato

    if articulo != None:
        
        # Modificamos descripcion y precio
        articulo.descripcion = descrip
        articulo.precio = price
    
        db_sqlite.session.commit() # Confirmar los cambios
        
        return True
    else:
        return False


       

    
    
