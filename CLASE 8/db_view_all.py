import db_sqlite
from db_articulos import Articulos

def view_all():
    # Obtener todos los registros de la tabla Articulos
    registros = db_sqlite.session.query(Articulos).all()

    # Iterar sobre los registros para imprimirlos
    for articulo in registros:
        print(articulo.codigo, articulo.descripcion, articulo.precio)



# db_sqlite.Base.metadata.create_all(db_sqlite.engine)
view_all()