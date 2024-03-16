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



def modify_articulos():
    # Consultar el registro con un código específico
    articulo = db_sqlite.session.query(Articulos).filter_by(codigo=9).first()

    # Modificar el precio
    articulo.precio = 14

    # Confirmar los cambios
    db_sqlite.session.commit()

