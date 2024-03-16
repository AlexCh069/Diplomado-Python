import db_sqlite
from db_articulos import Articulos

def run():

    articulo_add = Articulos(codigo=1, descripcion='fresa', precio=13)

    db_sqlite.session.add(articulo_add)
    db_sqlite.session.commit()

def view_all():
    # Obtener todos los registros de la tabla Articulos
    registros = db_sqlite.session.query(db_sqlite.Articulos).all()

    # Iterar sobre los registros para imprimirlos
    for articulo in registros:
        print(articulo.codigo, articulo.descripcion, articulo.precio)



db_sqlite.Base.metadata.create_all(db_sqlite.engine)
run()