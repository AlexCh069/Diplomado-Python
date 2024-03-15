# archivo: base_datos.py
from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///TUTORIALES LIBRERIAS/aplicacion.sqlite') # motor de base de datos
Session = sessionmaker(bind = engine)   # session
session = Session()
Base = declarative_base() 