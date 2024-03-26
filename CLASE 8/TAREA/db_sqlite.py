
# archivo: sd_sqlite.py

# Estructura de conexion con la base de datos usando el orm 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


engine = create_engine('sqlite:///aplicacion_tarea.sqlite')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
