from sqlalchemy import Column, Integer, String, ForeignKey
import base_datos

class Interprete(base_datos.Base):

    __tablename__ = 'interprete' # Nombre de tabla

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    cancion = Column(Integer, ForeignKey('cancion.id'))