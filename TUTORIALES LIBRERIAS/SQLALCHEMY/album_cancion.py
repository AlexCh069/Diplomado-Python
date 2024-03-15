from sqlalchemy import Column, Integer, ForeignKey
import base_datos

class AlbumCancion(base_datos.Base):
   __tablename__ = 'album_cancion'

   album = Column(Integer, ForeignKey('album.id'),primary_key=True)
   cancion = Column(Integer, ForeignKey('cancion.id'), primary_key=True)