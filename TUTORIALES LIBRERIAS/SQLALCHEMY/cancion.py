from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import base_datos


class Cancion(base_datos.Base):

    __tablename__ = 'cancion'               # Nombre de tabla 
    
    id = Column(Integer, primary_key=True)  # Primary Key (tmbn es un atributo)
    
    # Atributos (columnas )
    titulo = Column(String)
    minutos = Column(Integer)
    segundos = Column(Integer)
    compositor = Column(String)

    # albumes = relationship('Album', secondary= 'album_cancion')
    # interpretes = relationship('Interprete', cascade= 'all, delete, delete-orphan')

    def __init__(self, id, titulo, minutos, segundos, compositor):
        self.id = id
        self.titulo = titulo
        self.minutos = minutos
        self.segundos = segundos
        self.compositor = compositor
