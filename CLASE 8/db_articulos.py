from sqlalchemy import Column, Integer, String, Float

import db_sqlite

class Articulos(db_sqlite.Base):
    
    __tablename__ = 'articulo'  # nombre de la tabla

    # Atributos
    codigo = Column(Integer, primary_key=True, autoincrement= True)
    descripcion = Column(String)
    precio = Column(Float)

    def __init__(self, codigo, descripcion, precio):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio