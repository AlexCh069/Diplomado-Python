import db_sqlite
from db_articulos import Articulos

def modify_articulos():
    # Consultar el registro con un código específico
    articulo = db_sqlite.session.query(Articulos).filter_by(codigo=9).first()

    # Modificar el precio
    articulo.precio = 14

    # Confirmar los cambios
    db_sqlite.session.commit()


# db_sqlite.Base.metadata.create_all(db_sqlite.engine)
modify_articulos()